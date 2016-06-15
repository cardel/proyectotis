from django.conf.urls import url
from productortenant.views import ProductorForm, HomeView
from django.contrib import admin

#Urls publicas
urlpatterns = [
    url(r'^crea$', ProductorForm.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
]