from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from productortenant.forms import CrearProductorForm
from .models import Domain, Productor


import datetime

class Home(TemplateView):
    template_name = 'productortenant/inicio.html'

class Contacto(TemplateView):
    template_name = 'productortenant/contacto.html'

# Create your views here.
class CrearProductor(CreateView):
    template_name = 'productortenant/registrar.html'
    form_class = CrearProductorForm
    success_url = "/sucess"
    direccion = ''

    def form_valid(self, form):
        tenant_registrado = form.instance
        self.object = form.save()
        dominio = 'localhost'
        dominio_tenant = Domain(domain=self.object.schema_name+dominio,
                                is_primary=True,
                                tenant=tenant_registrado
                                )
        dominio_tenant.save()
        #Enviar al dominio
        self.direccion = self.object.schema_name+dominio

        return super(CrearProductor, self).form_valid(form)

    #Enviar parametros a la dirección de exito
    def get_context_data(self, **kwargs):
        ctx = super(CrearProductor, self).get_context_data(**kwargs)
        ctx['direccion'] = self.direccion
        return ctx

class MensajeExito(TemplateView):
    template_name = 'productortenant/exito.html'

def Mensaj22eExito(request):

    context = "";
    def get_context_data(self, **kwargs):
        context = super(MensajeExito, self).get_context_data(**kwargs)
        context['success'] = self.success
        return context


    return render(request, "exito.html", context)
