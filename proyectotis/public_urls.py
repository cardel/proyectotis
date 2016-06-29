from django.conf.urls import url
from productortenant.views import CrearProductor, MensajeExito, Home, Contacto, ReporteFincaView, ReporteProductosView, ReportesHomeView
from django.contrib import admin

#Urls publicas
urlpatterns = [
    url(r'^$', Home.as_view()),
    url(r'^crearFinca/', CrearProductor.as_view()),
    url(r'^contacto/', Contacto.as_view()),
    url(r'^sucess/', MensajeExito.as_view()),

    url(r'^admin/', admin.site.urls),


    ##Reportes
    url(r'^reportes/', ReportesHomeView.as_view()),
    url(r'^reportesProductos/', ReporteProductosView.as_view()),
    url(r'^reportesFinca/', ReporteFincaView.as_view()),

]