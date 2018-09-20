from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django_tenants.models import TenantMixin, DomainMixin


#Modelo para crear tenants
class Productor(TenantMixin):

    tipo_documento = models.CharField(max_length=3)
    identificacion = models.CharField(max_length=100, default=0,null=False)
    nombre = models.CharField(max_length=100, null=False)
    fecha_nacimiento =  models.DateField(null=False)
    telefono = models.CharField(max_length=100, null=False)
    correo = models.CharField(max_length=100, null=False)
    fecha_creacion = models.DateField(auto_now_add=True)

    # Esto crea automaticamente un esquema cuando se crea un productor
    auto_create_schema = True

    def __str__(self):
        return self.schema_name

class Domain(DomainMixin):
	pass

#Departamento

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

#Municipio
class Municipio(models.Model):
    #departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
