from django.shortcuts import render
from .models import Productor
from django.views.generic import TemplateView
from .forms import GenerateProductors
from tenant_schemas.utils import remove_www
from django.db import utils
from django.conf import settings


# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"

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