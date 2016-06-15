from django.db import models
from tenant_schemas.models import TenantMixin


#Modelo para crear tenants
class Productor(TenantMixin):
    document_choices = (
        ('CC', 'Cédula'),
        ('NIT', 'NIT'),
        ('OTHER', 'Otro'),
    )
    tipo_documento = models.CharField(
        max_length=3,
        choices=document_choices,
        default='CC'
    )
    nombre = models.CharField(max_length=100)
    fecha_nacimiento =  models.DateField()
    telefono = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    fecha_creacion = models.DateField(auto_now_add=True)

    # Esto crea automaticamente un esquema cuando se crea un productor
    auto_create_schema = True

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