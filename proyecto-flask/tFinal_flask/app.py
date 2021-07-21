from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Hola, Mundo!</p> \
    <a href='http://127.0.0.1:5000/laspersonas'>Personas</a> \
    - <a href='http://127.0.0.1:5000/losbarrios'>Barrios</a> \
    - <a href='http://127.0.0.1:5000/lascasas'>Casas</a> \
    - <a href='http://127.0.0.1:5000/losdepartamentos'>Departamentos</a>"


@app.route("/laspersonas")
def las_personas():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/personas/",
            auth=('jordy', '123456789'))
    personas = json.loads(r.content)
    numero_personas = len(personas)
    return render_template("laspersonas.html", personas=personas,
    numero_personas=numero_personas)

@app.route("/losbarrios")
def los_barrios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/barrios/",
            auth=('jordy', '123456789'))
    barrios = json.loads(r.content)
    numero_barrios = len(barrios)
    return render_template("losbarrios.html", barrios=barrios,
    numero_barrios=numero_barrios)

@app.route("/lascasas")
def las_casas():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/casas/",
            auth=('jordy', '123456789'))
    datos = json.loads(r.content)
    numero = len(datos)
    datos2 = []
    for d in datos:
        datos2.append({
            'propietario':obtener_persona(d['propietario']), 
            'direccion':d['direccion'],
            'barrio':obtener_barrio(d['barrio']),
            'valor':d['valor'],
            'color':d['color'],
            'cuartos':d['cuartos'],
            'pisos':d['pisos']})
    return render_template("lascasas.html", datos=datos2,
    numero=numero)

@app.route("/losdepartamentos")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamentos/",
            auth=('jordy', '123456789'))
    datos = json.loads(r.content)
    numero = len(datos)
    datos2 = []
    for d in datos:
        datos2.append({
            'propietario':obtener_persona(d['propietario']), 
            'direccion':d['direccion'],
            'barrio':obtener_barrio(d['barrio']),
            'valor_bien':d['valor_bien'],
            'cuartos':d['cuartos'],
            'valor_mensual':d['valor_mensual']})
    return render_template("losdepartamentos.html", datos=datos2,
    numero=numero)


# funciones ayuda
def obtener_persona(url):
    """
    """
    r = requests.get(url, auth=('jordy', '123456789'))
    persona = json.loads(r.content)['nombres'] + json.loads(r.content)['apellidos']
    return persona

def obtener_barrio(url):
    """
    """
    r = requests.get(url, auth=('jordy', '123456789'))
    barrio = json.loads(r.content)['nombre']
    return barrio

app.run()