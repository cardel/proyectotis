from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django_tenants.models import TenantMixin, DomainMixin


#Modelo para crear tenants
class Productor(TenantMixin):
    nombre_comercial = models.CharField(max_length=100, default='Ingrese una')
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

    def __str__(self):
        return self.schema_name

class Domain(DomainMixin):
    pass