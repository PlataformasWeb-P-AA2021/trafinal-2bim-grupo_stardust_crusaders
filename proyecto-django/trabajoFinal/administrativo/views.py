from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# ejemplo de uso django-rest_framework
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from administrativo.serializers import UserSerializer, GroupSerializer, \
PersonaSerializer, BarrioSerializer, CasaSerializer, DepartamentoSerializer

# importar las clases de models.py
from administrativo.models import *

# importar los formularios de forms.py 
from administrativo.forms import *

def index(request):
    """
    """
    personas = Persona.objects.all()

    informacion_template = {'personas': personas, 'numero_personas': len(personas)}
    return render(request, 'index.html', informacion_template)

def ingreso(request):

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.data.get("username")
            raw_password = form.data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect(index)
    else:
        form = AuthenticationForm()

    informacion_template = {'form': form}
    return render(request, 'registration/login.html', informacion_template)

def logout_view(request):
    logout(request)
    messages.info(request, "Has salido del sistema")
    return redirect(index)

@login_required(login_url='/entrando/login/')
def crear_persona(request):
    """
    """
    if request.method=='POST':
        formulario = PersonaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = PersonaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_persona.html', diccionario)

@login_required(login_url='/entrando/login/')
def editar_persona(request, id):
    """
    """
    persona = Persona.objects.get(pk=id)
    if request.method=='POST':
        formulario = PersonaForm(request.POST, instance=persona)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = PersonaForm(instance=persona)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_persona.html', diccionario)

@login_required(login_url='/entrando/login/')
def eliminar_persona(request, id):
    """
    """
    persona = Persona.objects.get(pk=id)
    persona.delete()
    return redirect(index)

@login_required(login_url='/entrando/login/')
def crear_barrio(request):
    """
    """
    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_barrio.html', diccionario)

@login_required(login_url='/entrando/login/')
def editar_barrio(request, id):
    """
    """
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_barrio.html', diccionario)

@login_required(login_url='/entrando/login/')
def eliminar_barrio(request, id):
    """
    """
    barrio = Barrio.objects.get(pk=id)
    barrio.delete()
    return redirect(index)

@login_required(login_url='/entrando/login/')
def crear_casa(request):
    """
    """
    if request.method=='POST':
        formulario = CasaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = CasaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_casa.html', diccionario)

@login_required(login_url='/entrando/login/')
@permission_required('administrativo.update_casa', login_url="/entrando/login/")
def editar_casa(request, id):
    """
    """
    casa = Casa.objects.get(pk=id)
    if request.method=='POST':
        formulario = CasaForm(request.POST, instance=casa)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = CasaForm(instance=casa)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_casa.html', diccionario)

@login_required(login_url='/entrando/login/')
@permission_required('administrativo.delete_casa', login_url="/entrando/login/")
def eliminar_casa(request, id):
    """
    """
    casa = Casa.objects.get(pk=id)
    casa.delete()
    return redirect(index)

@login_required(login_url='/entrando/login/')
def crear_casa_persona(request, id):
    """
    """
    propietario = Persona.objects.get(pk=id)
    if request.method=='POST':
        formulario = CasaPersonaForm(propietario, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = CasaPersonaForm(propietario)
    diccionario = {'formulario': formulario, 'propietario': propietario}

    return render(request, 'crear_casa_persona.html', diccionario)

@login_required(login_url='/entrando/login/')
def crear_departamento(request):
    """
    """
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_departamento.html', diccionario)

@login_required(login_url='/entrando/login/')
@permission_required('administrativo.update_departamento', login_url="/entrando/login/")
def editar_departamento(request, id):
    """
    """
    departamento = Departamento.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST, instance=departamento)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm(instance=departamento)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_departamento.html', diccionario)

@login_required(login_url='/entrando/login/')
@permission_required('administrativo.delete_departamento', login_url="/entrando/login/")
def eliminar_departamento(request, id):
    """
    """
    departamento = Departamento.objects.get(pk=id)
    departamento.delete()
    return redirect(index)

@login_required(login_url='/entrando/login/')
def crear_departamento_persona(request, id):
    """
    """
    propietario = Persona.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoPersonaForm(propietario, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoPersonaForm(propietario)
    diccionario = {'formulario': formulario, 'propietario': propietario}

    return render(request, 'crear_departamento_persona.html', diccionario)

def listar_casas(request):
    """
    """
    casas = Casa.objects.all()

    informacion_template = {'casas': casas, 'numero_casas': len(casas)}
    return render(request, 'listar_casas.html', informacion_template)

def listar_departamentos(request):
    """
    """
    departamentos = Departamento.objects.all()

    informacion_template = {'departamentos': departamentos, 'numero_casas': len(departamentos)}
    return render(request, 'listar_departamentos.html', informacion_template)

def listar_barrios(request):
    """
    """
    barrios = Barrio.objects.all()

    informacion_template = {'barrios': barrios, 'numero_barrios': len(barrios)}
    return render(request, 'listar_barrios.html', informacion_template)

# crear vistas a través de viewsets
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PersonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    # permission_classes = [permissions.IsAuthenticated]

class BarrioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer
    # permission_classes = [permissions.IsAuthenticated]

class CasaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Casa.objects.all()
    serializer_class = CasaSerializer
    # permission_classes = [permissions.IsAuthenticated]

class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    # permission_classes = [permissions.IsAuthenticated]