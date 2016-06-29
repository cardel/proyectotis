from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required


# Create your views here.

from .forms import RegistradoForm, RegistradoFruta
from .models import RegistrarFruta, RegistrarFinca



class Home(TemplateView):
    template_name = 'gestionfruta/inicio.html'



##Borrar
def inicio(request):
    titulo = "Registro Datos Fruta"
    form = RegistradoForm(request.POST or None)

    if form.is_valid():
        form.save()


    tituloFinca = "Registro datos Finca"
    formFinca = RegistradoFruta(request.POST or None)

    if formFinca.is_valid():
        formFinca.save()

    context = {
        "titulo": titulo,
        "form": form,

        "tituloFruta": tituloFinca,
        "formFinca": formFinca,

    }

    return render(request, "index.html", context)

