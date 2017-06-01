"""proyectotis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from gestionfruta.views import Home, RegistrarFincaView, RegistrarFrutaView, EditarFincaView, EditarFrutaView, AdminContactoView, EditarContactoView, FincaView, FrutaView, ContactoView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout

urlpatterns = [

    url(r'^$', Home.as_view()),

    url(r'^adminfinca/$', RegistrarFincaView.as_view()),
    url(r'^editarFinca/(?P<pk>\d+)/$', EditarFincaView.as_view()),

    url(r'^adminfruta/$', RegistrarFrutaView.as_view()),
    url(r'^editarFruta/(?P<pk>\d+)/$', EditarFrutaView.as_view()),

    url(r'^adminContacto/$', AdminContactoView.as_view()),
    url(r'^editarContacto/(?P<pk>\d+)/$', EditarContactoView.as_view()),

    #Publicos
    url(r'^finca/$', FincaView.as_view()),
    url(r'^fruta/$', FrutaView.as_view()),
    url(r'^contacto/$', ContactoView.as_view()),



    #Autenticacion
    url(r'^login/$', login, {'template_name': 'gestionfruta/login.html'}, name='mysite_login'),
    url(r'^logout/$', logout,  {'next_page': "/"}, name='mysite_logout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

