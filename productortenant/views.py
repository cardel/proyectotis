from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from productortenant.forms import CrearProductorForm
from .models import Domain, Productor
from django.contrib.auth.models import User
from django.db import connection

from django.core import serializers

#Para los reportes
from gestionfruta.models import Fruta, Finca

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
        dominio = "proyectotis.com"
        tenant_registrado = form.instance
        self.object = form.save()
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


### Reportes ####
class ReportesHomeView(TemplateView):
    template_name = 'productortenant/reportes/homeReportes.html'

class ReporteProductosView(TemplateView):
    template_name = 'productortenant/reportes/reportesProductos.html'

    def get_context_data(self, **kwargs):
        context = super(ReporteProductosView, self).get_context_data(**kwargs)
        reporte = []
        tenants = Productor.objects.exclude(schema_name='public')
        dominio = "proyectotis.com:8080"


        #Reportes gráficos
        productoPorAltura = {}
        productoPorTemperatura = {}
        productosTotales = {}

        for tenant in tenants:
            connection.set_tenant(tenant)


            listaNombreFrutas = Fruta.objects.values_list('nombre')
            listamsnmFrutas = Fruta.objects.values_list('msnm')
            listaTemperaturaFrutas = Fruta.objects.values_list('temperatura')

            for fruta in listaNombreFrutas:

                f = str(fruta[0]).capitalize()

                if f in productosTotales:
                    productosTotales[f]=productosTotales[f]+1
                else:
                    productosTotales[f]=1


            for fruta in listamsnmFrutas:

                f =fruta[0]
                if f in productoPorAltura:
                    productoPorAltura[f]=productoPorAltura[f]+1
                else:
                    productoPorAltura[f]=1

            for fruta in listaTemperaturaFrutas:

                f =fruta[0]
                if f in productoPorTemperatura:
                    productoPorTemperatura[f]=productoPorTemperatura[f]+1
                else:
                    productoPorTemperatura[f]=1

            reporte_actual = {
                'url': tenant.schema_name+'.'+dominio,
                'info': serializers.serialize("python", Fruta.objects.all())
            }

            reporte.append(reporte_actual)


        reportesGenerados = {
            'reporteTotalNombre': productosTotales,
            'reporteTotalAltura': productoPorAltura,
            'reporteTotalTemperatura': productoPorTemperatura,

        }

        connection.set_schema_to_public()

        contexto = {
            'reporte' : reporte,
            'reportesGenerados' : reportesGenerados,
        }

        context.update(contexto)
        return context

class ReporteFincaView(TemplateView):
    template_name = 'productortenant/reportes/reportesFinca.html'

    def get_context_data(self, **kwargs):
        dominio = "proyectotis.com:8080"
        context = super(ReporteFincaView, self).get_context_data(**kwargs)
        reporte = []
        tenants = Productor.objects.exclude(schema_name='public')

        for tenant in tenants:
            connection.set_tenant(tenant)
            reporte_actual = {
                'url': tenant.schema_name+'.'+dominio,
                'info': serializers.serialize("python", Finca.objects.all())
            }

            reporte.append(reporte_actual)


        connection.set_schema_to_public()

        contexto = {
            'reporte' : reporte
        }

        context.update(contexto)
        return context

