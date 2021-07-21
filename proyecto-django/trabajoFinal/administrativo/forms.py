from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Persona, \
        Barrio, Casa, Departamento

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombres', 'apellidos', 'cedula', 'correo']
        labels = {
            'nombres': _('Ingrese nombre por favor'),
            'apellidos': _('Ingrese apellido por favor'),
            'cedula': _('Ingrese cédula por favor'),
            'correo': _('Ingrese correo por favor'),
        }

class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'siglas']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'siglas': _('Ingrese siglas por favor'),
        }

class CasaForm(ModelForm):
    class Meta:
        model = Casa
        fields = ['propietario', 'direccion', 'barrio', 'valor', 'color', 'cuartos', 'pisos']

class CasaPersonaForm(ModelForm):

    def __init__(self, persona, *args, **kwargs):
        super(CasaPersonaForm, self).__init__(*args, **kwargs)
        self.initial['propietario'] = persona
        self.fields["propietario"].widget = forms.widgets.HiddenInput()
        print(persona)

    class Meta:
        model = Casa
        fields = ['propietario', 'direccion', 'barrio', 'valor', 'color', 'cuartos', 'pisos']


class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['propietario', 'direccion', 'barrio', 'valor_bien', 'cuartos', 'valor_mensual']

class DepartamentoPersonaForm(ModelForm):

    def __init__(self, persona, *args, **kwargs):
        super(DepartamentoPersonaForm, self).__init__(*args, **kwargs)
        self.initial['propietario'] = persona
        self.fields["propietario"].widget = forms.widgets.HiddenInput()
        print(persona)

    class Meta:
        model = Departamento
        fields = ['propietario', 'direccion', 'barrio', 'valor_bien', 'cuartos', 'valor_mensual']