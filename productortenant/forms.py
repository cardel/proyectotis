#Formularios del tenant, es productor
from django import forms
from .models import Productor


class ProductorForm(forms.ModelForm):
    class RegistrarTenant:
        model = Productor
        fields = ["nombre comercial", "tipo_documento", "nombre", "fecha_nacimiento", "telefono", "correo"]

    def clean_email(self):
        nombre = self.cleaned_data.get("nombre")
        return nombre


