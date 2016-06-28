from django.conf.urls import url
from productortenant.views import CrearProductor, MensajeExito, Home, Contacto
from django.contrib import admin

#Urls publicas
urlpatterns = [
    url(r'^$', Home.as_view()),
    url(r'^crearFinca/', CrearProductor.as_view()),
    url(r'^contacto/', Contacto.as_view()),
    url(r'^sucess/', MensajeExito.as_view()),

    url(r'^admin/', admin.site.urls),
]