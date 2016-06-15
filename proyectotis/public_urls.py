from django.conf.urls import url
from productortenant.views import CrearProductor
from django.contrib import admin

#Urls publicas
urlpatterns = [
    url(r'^productor/', CrearProductor.as_view()),
    url(r'^admin/', admin.site.urls),
]