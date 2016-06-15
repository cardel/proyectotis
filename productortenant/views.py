from django.shortcuts import render
from .forms import ProductorForm

# Create your views here.

def inicio(request):
    titulo = "Registro Productor"
    form = ProductorForm(request.POST or None)

    if form.is_valid():
        form.save()


    context = {
        "titulo": titulo,
        "form": form
    }