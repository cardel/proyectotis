from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from productortenant.forms import CrearProductorForm
from .models import Domain, Productor
from django.contrib.auth.models import User
from django.db import connection


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

    def form_valid(self, form):
        tenant_registrado = form.instance
        self.object = form.save()
        dominio = 'localhost'
        dominio_tenant = Domain(domain=self.object.schema_name+'.'+dominio,
                                is_primary=True,
                                tenant=tenant_registrado
                                )
        dominio_tenant.save()

        #Enviar parametros
        self.request.session['direccion'] = self.object.schema_name+'.'+dominio
        #Enviar al dominio

        #Vamos a crear un usuario en el tenant
        tenants = Productor.objects.get(schema_name=self.object.schema_name)

        connection.set_tenant(tenants)
        user = User.objects.create_user(form.cleaned_data['usuario'], form.cleaned_data['correo'], form.cleaned_data['password'])
        user.save()

        connection.set_schema_to_public()
        return super(CrearProductor, self).form_valid(form)



class MensajeExito(TemplateView):
    template_name = 'productortenant/exito.html'

