"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('crear/persona', views.crear_persona, name='crear_persona'),
    path('editar/persona/<int:id>', views.editar_persona, name='editar_persona'),
    path('eliminar/persona/<int:id>', views.eliminar_persona, name='eliminar_persona'),
    path('crear/barrio', views.crear_barrio, name='crear_barrio'),
    path('editar/barrio/<int:id>', views.editar_barrio, name='editar_barrio'),
    path('eliminar/barrio/<int:id>', views.eliminar_barrio, name='eliminar_barrio'),
    path('crear/casa', views.crear_casa, name='crear_casa'),
    path('editar/casa/<int:id>', views.editar_casa, name='editar_casa'),
    path('eliminar/casa/<int:id>', views.eliminar_casa, name='eliminar_casa'),
    path('crear/casa_persona/<int:id>',
            views.crear_casa_persona,
            name='crear_casa_persona'),
    path('crear/departamento', views.crear_departamento, name='crear_departamento'),
    path('editar/casa/<int:id>', views.editar_departamento, name='editar_departamento'),
    path('eliminar/departamento/<int:id>', views.eliminar_departamento, name='eliminar_departamento'),
    path('crear/departamento_persona/<int:id>',
            views.crear_departamento_persona,
            name='crear_departamento_persona'),
    path('listar/casas', views.listar_casas, name='listar_casas'),
    path('listar/departamentos', views.listar_departamentos, name='listar_departamentos'),
    path('listar/barrios', views.listar_barrios, name='listar_barrios'),
    path('saliendo/logout/', views.logout_view, name="logout_view"),
    path('entrando/login/', views.ingreso, name="login"),
]
