from django.conf.urls import url

from productortenant.views import ProductorForm
from django.contrib import admin

#Urls publicas
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ProductorForm.as_view()),

]