from django.conf.urls import url
from productortenant.views import CrearProductor, MensajeExito
from django.contrib import admin

#Urls publicas
urlpatterns = [
    url(r'^$', CrearProductor.as_view()),
    url(r'^creado/',  'productortenant.views.MensajeExito', name='inicio'),
    url(r'^admin/', admin.site.urls),

]