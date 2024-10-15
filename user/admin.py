from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin 

# Register your models here.

admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    
    # Personalizar nombres de filtros
    #list_filter = (
       # ('is_staff', admin.BooleanFieldListFilter),
        #('is_superuser', admin.BooleanFieldListFilter),
        #('is_active', admin.BooleanFieldListFilter),
    #)
    
    # Agrega opciones para búsqueda (si decides mantenerlo)
    # search_fields = ('username', 'email', 'first_name', 'last_name')

    # Mejora las acciones (por ejemplo, permite la eliminación de varios usuarios)
    actions = ['delete_selected']

    # Agrega instrucciones para que el usuario sepa qué puede hacer
    def get_list_display(self, request):
        return self.list_display

    def get_list_filter(self, request):
        return self.list_filter

    # Mensaje en la parte superior
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'User Management'}  # Título más claro
        return super().changelist_view(request, extra_context=extra_context)
    
    class Media:
        css = {
            'all': ('admin/admin_custom.css',)  # Ruta del archivo CSS personalizado
        }

admin.site.unregister(User)
admin.site.register(User, UserAdmin)