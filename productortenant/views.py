from django.shortcuts import render
from .models import Productor, Domain
from django.views.generic import CreateView


# Create your views here.
class CrearProductor(CreateView):
    model = Productor
    success_url = "/gg"
    fields = ["tipo_documento", "url", "nombre", "fecha_nacimiento", "telefono", "correo"]

    def form_valid(self,form):
        tenant_registrado = form.instance
        tenant_registrado.schema_name = tenant_registrado.nombreurl
        self.object = form.save()
        dominio_tenant = Domain(domain=self.object.nombre_tenant+'.localhost',
                                is_primary=True,
                                tenant=tenant_registrado
                                )
        dominio_tenant.save()
        return super(CrearProductor, self).form_valid(form)

