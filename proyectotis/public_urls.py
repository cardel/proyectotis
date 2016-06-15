from django.conf.urls import url

from productortenant.views import ProductorForm
#Urls publicas
urlpatterns = [
   url(r'^$', ProductorForm.as_view()),

]