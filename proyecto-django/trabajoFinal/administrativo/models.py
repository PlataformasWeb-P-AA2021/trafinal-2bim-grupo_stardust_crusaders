from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    correo = models.EmailField()

    def __str__(self):
        return "%s %s %s %s" % (self.nombres,
                self.apellidos,
                self.cedula,
                self.correo)

class Barrio(models.Model):
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.nombre,
                self.siglas)

class Casa(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE,
            related_name="casa_persona")
    direccion = models.CharField(max_length=50)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE,
            related_name="casa_barrio")
    valor = models.IntegerField()
    color = models.CharField(max_length=30)
    cuartos = models.IntegerField()
    pisos = models.IntegerField()

    def __str__(self):
        return "%s %d %s %d %d" % (self.direccion, 
        self.valor,
        self.color,
        self.cuartos,
        self.pisos)

class Departamento(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE,
            related_name="departamento_persona")
    direccion = models.CharField(max_length=50)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE,
            related_name="departamento_barrio")
    valor_bien = models.IntegerField()
    cuartos = models.IntegerField()
    valor_mensual = models.IntegerField()

    def __str__(self):
        return "%s %d %d %d" % (self.direccion, 
        self.valor_bien,
        self.cuartos,
        self.valor_mensual)