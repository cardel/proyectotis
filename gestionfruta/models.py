from django.db import models


# Este modelo va relacionado con el productor.
class Registrado(models.Model):
    nombre = models.CharField(max_length=120, blank=True, null=True)
    variedad = models.CharField(max_length=120, default="")
    areacultivo = models.CharField(max_length=120, default="")
    produccionmes = models.IntegerField(default=0)
    tipoterreno = models.CharField(max_length=120, default="")
    msnm = models.IntegerField(default=0)
    temperatura = models.IntegerField(default=0)
    def __unicode__(self):
        return self.nombre