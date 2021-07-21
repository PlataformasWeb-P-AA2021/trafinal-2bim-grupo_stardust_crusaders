from django.contrib import admin

from administrativo.models import Persona, Barrio, Casa, Departamento

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'cedula', 'correo')
    search_fields = ('nombre', 'cedula')

admin.site.register(Persona, PersonaAdmin)

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas')
    search_fields = ('nombre',)

admin.site.register(Barrio, BarrioAdmin)

class CasaAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'direccion', 'barrio', 'valor', 'color', 'cuartos', 'pisos')
    raw_id_fields = ('propietario', 'barrio')

admin.site.register(Casa, CasaAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'direccion', 'barrio', 'valor_bien', 'cuartos', 'valor_mensual')
    raw_id_fields = ('propietario', 'barrio')

admin.site.register(Departamento, DepartamentoAdmin)