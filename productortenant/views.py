from django.shortcuts import render
from .models import Domain, Productor
from django.views.generic import FormView, TemplateView
from .forms import GenerateProductors
from django_tenants.utils import remove_www


# Create your views here.
class ProductorForm(FormView):
    form_class = GenerateProductors
    success_url = "/"
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

class HomeView(TemplateView):
    template_name = "index_public.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        hostname_without_port = remove_www(self.request.get_host().split(':')[0])

        try:
            Productor.objects.get(schema_name='public')
        except utils.DatabaseError:
            context['need_sync'] = True
            context['shared_apps'] = settings.SHARED_APPS
            context['tenants_list'] = []
            return context
        except Productor.DoesNotExist:
            context['no_public_tenant'] = True
            context['hostname'] = hostname_without_port

        if Productor.objects.count() == 1:
            context['only_public_tenant'] = True

        context['tenants_list'] = Productor.objects.all()
        return context