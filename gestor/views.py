
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.models import User
from django.contrib import messages
import re
from django.contrib.auth import authenticate, login as auth_login, logout
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.views.decorators.csrf import csrf_exempt
from user.models import Proyecto, MiembrosProyectos, Roles
from django.shortcuts import get_object_or_404
#----------------Inicio----------------
def home(request):
    return render(request, 'index.html')

#----------------Login----------------
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Inicio sesion correctamente.')
            return redirect('home')  # Redirige a la vista de proyectos si el login es exitoso
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
    return render(request, 'login.html')

#----------------Registro----------------
@csrf_exempt
def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        location = request.POST.get('location', '').strip()  # Asegúrate de que 'location' sea capturado
        number_phone = request.POST.get('number_phone', '').strip()
        

        # Validar que el nombre de usuario no contenga números
        if any(char.isdigit() for char in username):
            messages.error(request, 'El nombre de usuario no puede contener números.')
            return render(request, 'registro.html')

        # Validar que la contraseña tenga entre 7 y 20 caracteres
        if len(password) < 7 or len(password) > 20:
            messages.error(request, 'La contraseña debe tener entre 7 y 20 caracteres.')
            return render(request, 'registro.html')
        
        # Validar que la contraseña coincida con la confirmación
        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'registro.html')

        # Validar que el email sea un correo
        try:
            validate_email(email)  # Verifica el email
        except ValidationError:
            messages.error(request, 'El email no cumple con los parámetros @.')
            return render(request, 'registro.html')

        # Verifica usuario y email
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso. Por favor, elige otro.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está registrado. Por favor, usa otro.')
        else:
            # Crea el usuario si no están en uso
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            auth_login(request, user)
            messages.success(request, 'Registrado correctamente.')
            return redirect('home')  # Redirige a la vista 'home' después del registro exitoso

    return render(request, 'registro.html')

#-----------ver los proyectos------------
def verproyectos(request):
    return render(request, 'verproyectos.html')


#-----------------Usuarios---------------
@login_required(login_url="login")
def verusuarios(request):
    return render(request,'usuarios.html')



#----------------LOGOUT----------------
def exit(request):
        logout(request)
        return redirect('home')


#----------------Actualizar perfil----------------

@login_required(login_url="login")
def actualizarperfil(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        number_phone = request.POST.get('number_phone')
        location = request.POST.get('location')
        password = request.POST.get('password')
        current_password = request.POST.get('current_password')  # Campo para la contraseña actual

        user = request.user
        if username != user.username or email != user.email or number_phone != user.number_phone or location != user.location or password:
            # Validaciones
            if username != user.username:
                if not re.match(r'^[a-zA-Z]{8,50}$', username):
                    messages.error(request, 'El nombre de usuario debe tener entre 8 y 50 caracteres y no puede contener espacios ni números.')
                    return redirect('actualizar_perfil')

            if email != user.email:
                if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                    messages.error(request, 'Por favor, ingresa un correo electrónico válido.')
                    return redirect('actualizar_perfil')

            if password and (len(password) < 7 or len(password) > 20):
                messages.error(request, 'La contraseña debe tener entre 7 y 20 caracteres.')
                return redirect('actualizar_perfil')

            if number_phone != user.number_phone:
                if not re.match(r'^\d{2}\d{10}$', number_phone):
                    messages.error(request, 'El número de teléfono debe tener 12 dígitos, incluyendo el código de país.')
                    return redirect('actualizar_perfil')

            if location != user.location:
                if not re.match(r'^[a-zA-Z\s]{4,20}$', location):
                    messages.error(request, 'El lugar de residencia debe tener entre 4 y 20 caracteres y no incluir caracteres especiales.')
                    return redirect('actualizar_perfil')

            # Verificación de contraseña actual antes de cambiarla
            if password:
                if current_password:
                    if not user.check_password(current_password):
                        messages.error(request, 'La contraseña actual no es correcta.')
                        return redirect('actualizar_perfil')
                    user.set_password(password)
                    
                else:
                    messages.error(request, 'Ingrese la contraseña actual para cambiar la contraseña')
                    return redirect('actualizar_perfil')

            # Actualizar los campos del usuario
            user.username = username
            user.email = email
            user.number_phone = number_phone
            user.location = location
            user.save()
            auth_login(request, user)

            messages.success(request, 'Tu perfil ha sido actualizado exitosamente.')
            return redirect('proyectos')  # Redirige de vuelta a la página de perfil
        else:
            messages.info(request, 'No hubo ningun cambio en tu perfil.')
            return redirect('proyectos')  # Redirige de vuelta a la página de perfil

    return render(request, 'perfilconfig.html')  # Asegúrate de que este nombre coincida con tu archivo de plantilla

#----------------Vista de proyectos----------------
@login_required(login_url="login")
def proyectos(request):
    if request.method == 'POST':
        # Recoger datos del formulario
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        # Validar que todos los campos están llenos
        if nombre and descripcion and fecha_inicio and fecha_fin:
            try:
                # Crear y guardar el proyecto usando el modelo Proyecto
                proyecto = Proyecto(
                    nombre=nombre,
                    descripcion=descripcion,
                    fecha_inicio=fecha_inicio,
                    fecha_fin=fecha_fin
                )
                proyecto.save()
                
                # Asociar al usuario actual con el proyecto
                miembro_proyecto = MiembrosProyectos(
                    usuario=request.user,
                    proyecto=proyecto,
                    rol=Roles.objects.get(rol='Administrador del departamento')  # Asigna un rol por defecto o personalizado
                )
                miembro_proyecto.save()
                
                messages.success(request, 'Proyecto creado exitosamente.')
            except Exception as e:
                messages.error(request, f'Ocurrió un error al crear el proyecto: {e}')
        else:
            messages.error(request, 'Por favor, rellene todos los campos.')
        return redirect('proyectos')  # Redirige de vuelta a la página de perfil

    # Obtener los proyectos en los que el usuario es miembro
    proyectos_usuario = Proyecto.objects.filter(
        id__in=MiembrosProyectos.objects.filter(usuario=request.user).values('proyecto')
    )

    # Pasar los proyectos al contexto de la plantilla
    context = {
        'proyectos_usuario': proyectos_usuario
    }

    return render(request, 'vistaprojectos.html', context)

#----------------Definir ver proyectos--------------------------
@login_required(login_url="login")
def verproyectos(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)

    # Obtener los miembros del proyecto
    miembros = MiembrosProyectos.objects.filter(proyecto=proyecto).exclude(usuario=request.user)

    if request.method == 'POST':
        # Acción para agregar un usuario
        if 'agregar_usuario' in request.POST:
            correo = request.POST.get('correo')
            rol = request.POST.get('rol')

            try:
                usuario = User.objects.get(email=correo)
                rol_obj = Roles.objects.get(rol=rol)
                # Verificar si el usuario ya está en el proyecto
                if not MiembrosProyectos.objects.filter(usuario=usuario, proyecto=proyecto).exists():
                    MiembrosProyectos.objects.create(usuario=usuario, proyecto=proyecto, rol=rol_obj)
                    messages.success(request, f"Usuario {usuario.email} agregado al proyecto.")
                else:
                    messages.warning(request, f"El usuario {usuario.email} ya forma parte del proyecto.")
            except User.DoesNotExist:
                messages.error(request, f"No se encontró un usuario con el correo {correo}.")
            except Roles.DoesNotExist:
                messages.error(request, f"El rol {rol} no existe.")
        
        # Acción para eliminar un usuario
        elif 'eliminar_usuario' in request.POST:
            miembro_id = request.POST.get('miembro_id')
            MiembrosProyectos.objects.filter(id=miembro_id).delete()
            messages.success(request, "El usuario fue eliminado del proyecto.")

        # Acción para actualizar el rol de un usuario
        elif 'cambiar_rol' in request.POST:
            miembro_id = request.POST.get('miembro_id')
            nuevo_rol = request.POST.get('rol')
            try:
                miembro = MiembrosProyectos.objects.get(id=miembro_id)
                rol_obj = Roles.objects.get(rol=nuevo_rol)
                # Verificar si el rol actual es diferente del nuevo rol
                if miembro.rol != rol_obj:
                    miembro.rol = rol_obj
                    miembro.save()
                    messages.success(request, f"El rol de {miembro.usuario.email} se ha actualizado a {nuevo_rol}.")
                else:
                    messages.info(request, f"El usuario {miembro.usuario.email} ya tiene el rol {nuevo_rol}.")
            except MiembrosProyectos.DoesNotExist:
                messages.error(request, "No se pudo encontrar el miembro del proyecto.")
            except Roles.DoesNotExist:
                messages.error(request, "El rol seleccionado no existe.")

        return redirect('verproyectos', id=id)

    context = {
        'proyecto': proyecto,
        'miembros': miembros,
        'roles': Roles.objects.exclude(rol='Administrador del departamento'),  # Pasamos los roles disponibles para el selector
    }

    return render(request, 'verproyectos.html', context)




