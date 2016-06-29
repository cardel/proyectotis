from django.db import models
import uuid

#Esta funcion agrega una ruta al tenant
#Crea una carpeta aleatoria para evitar los usuarios se coman entre sí
def rutaArchivoTenant(self, file):
    url = "imagesites/%s/%s" % (uuid.uuid4(), file)
    return url

# Este modelo son las frutas que se producen en la fica
class Fruta(models.Model):
    nombre = models.CharField(max_length=120, default="")
    variedad = models.CharField(max_length=120, default="")
    areacultivo = models.CharField(max_length=120, default="")
    produccionmes = models.IntegerField(default=0)
    tipoterreno = models.CharField(max_length=120, default="")
    msnm = models.IntegerField(default=0)
    temperatura = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to=rutaArchivoTenant, null=True)
    def __unicode__(self):
        return self.nombre


#Registrar finca

class Finca(models.Model):

    nombre = models.CharField(max_length=120, blank=True, null=True)
    municipio = models.CharField(max_length=120, blank=True, null=True)
    departamento = models.CharField(max_length=100,null=True)
    imagen = models.ImageField(upload_to=rutaArchivoTenant, null=True, default="")
    descripcion = models.TextField(blank=False)
    def __unicode__(self):
        return self.nombre


#Contacto
class Contacto(models.Model):

    direccion = models.CharField(max_length=120, blank=True, null=False, default="")
    telefono = models.CharField(max_length=120, blank=True, null=False, default="")
    email = models.EmailField(blank=True, null=False, default="")


#Registrar