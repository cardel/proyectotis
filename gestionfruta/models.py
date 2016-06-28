from django.db import models


# Este modelo va relacionado con el productor.
class RegistrarFruta(models.Model):
    nombre = models.CharField(max_length=120, blank=True, null=True)
    variedad = models.CharField(max_length=120, default="")
    areacultivo = models.CharField(max_length=120, default="")
    produccionmes = models.IntegerField(default=0)
    tipoterreno = models.CharField(max_length=120, default="")
    msnm = models.IntegerField(default=0)
    temperatura = models.IntegerField(default=0)
    def __unicode__(self):
        return self.nombre


#Registrar finca

class RegistrarFinca(models.Model):

    departament_choices = (
        ('Bogota', 'Bogota'),
        ('Valle', 'Valle'),
        ('Antioquia', 'Antioquia'),
        ('Cauca', 'Cauca'),
        ('Santander', 'Santander'),
        ('Guajira', 'Guajira'),
        ('Amazonas', 'Amazonas'),
        ('Huila', 'Huila'),
        ('Putumayo', 'Putumayo'),
    )

    nombre = models.CharField(max_length=120, blank=True, null=True)
    municipio = models.CharField(max_length=120, blank=True, null=True)
    departamento = models.CharField(
        max_length=100,
        choices=departament_choices,
        default='Valle'
    )
    descripcion = models.TextField(blank=True)


    def __unicode__(self):
        return self.nombre




#Registrar