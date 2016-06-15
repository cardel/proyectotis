from django.shortcuts import render

# Create your views here.

from .forms import RegistradoForm
from .models import Registrado


def inicio(request):
    titulo = "Registro Datos Fruta"
    form = RegistradoForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        "titulo": titulo,
        "form": form
    }

    return render(request, "templateProyecto/index.html", context)

