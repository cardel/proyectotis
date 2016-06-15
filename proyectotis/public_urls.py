from django.conf.urls import url

import gestionfruta

#Urls propias de la aplicación
#1. Registrar fruta
urlpatterns = [
    url(r'^$', gestionfruta.views.inicio, name='inicio'),
]