from django.shortcuts import render
from .forms import ProductorForm
from .models import Domain

# Create your views here.
def registrarProductor(request):
    titulo = "Registro Productor"
    form = ProductorForm(request.POST or None)

    if form.is_valid():
        tenant_registrado = form.instance
        tenant_registrado.schema_name = tenant_registrado.nombre_tenant
        formulario = form.save()
        dominio_tenant = Domain(formulario.nombre_comercial+'.localhost',
                                is_primary=True,
                                tenant=tenant_registrado
                                )
        dominio_tenant.save()
        form.save()

    context = {
        "titulo": titulo,
        "form": form
    }