from django.conf.urls import url
from productortenant.views import ProductorForm
from django.contrib import admin

#Urls publicas
urlpatterns = [
    url(r'^$', ProductorForm.as_view()),
    url(r'^admin/', admin.site.urls),
]