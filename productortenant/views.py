from django.shortcuts import render
from .models import Domain, Productor
from django.views.generic import FormView
from .forms import GenerateProductors


# Create your views here.
class ProductorForm(FormView):
    form_class = GenerateProductors
    success_url = "/jaja"
    template_name = "index.html"
    titulo = "Registro Productor"
    model = Productor
    fields = ["tipo_documento", "dominio", "nombre", "fecha_nacimiento", "telefono", "correo"]

    def get_context_data(self, **kwargs):
        context = super(ProductorForm, self).get_context_data(**kwargs)
        return context

    def form_valid(self,form):
        tenant_registrado = form.instance
        tenant_registrado.schema_name = tenant_registrado.domain_url
        self.object = form.save()
        dominio_tenant = Domain(domain=self.object.nombre_tenant+'.localhost',
                                is_primary=True,
                                tenant=tenant_registrado
                                )
        dominio_tenant.save()
        return super(ProductorForm, self).form_valid(form)

