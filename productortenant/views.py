from django.shortcuts import render
from .models import Productor, Domain
from django.views.generic import CreateView,TemplateView
import datetime


# Create your views here.
class CrearProductor(CreateView):
    model = Productor
    success_url = "/creado"
    fields = ["tipo_documento","identificacion", "url", "nombre", "fecha_nacimiento", "telefono", "correo"]


    def form_valid(self,form):
        dominio = "localhost"
        tenant_registrado = form.instance
        tenant_registrado.schema_name = tenant_registrado.url
        tenant_registrado.domain_url = tenant_registrado.url
        self.object = form.save()
        dominio_tenant = Domain(domain=self.object.url+"."+dominio,
                                is_primary=True,
                                tenant=tenant_registrado
                                )
        dominio_tenant.save()

        #Enviar el request
        self.request.session['direccion'] = tenant_registrado.domain_url+"."+dominio

        return super(CrearProductor, self).form_valid(form)





def MensajeExito(request):

    context = "";
    def get_context_data(self, **kwargs):
        context = super(MensajeExito, self).get_context_data(**kwargs)
        context['success'] = self.success
        return context


    return render(request, "exito.html", context)
