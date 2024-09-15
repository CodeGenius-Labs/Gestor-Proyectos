from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('login/', views.login, name='login'),
    #path('accounts/', include ('django.contrib.auth.urls')),
    path('registro/', views.registro, name='registro'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('perfil/',views.actualizarperfil, name='actualizar_perfil'),
    path('logout/',views.exit, name='logout'),
    path('verproyectos/<int:id>/', views.verproyectos, name='verproyectos'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
