from django import forms
from .models import RegistrarFruta, RegistrarFinca

#Formulario de registrar producto
class RegistradoForm(forms.ModelForm):
    class Meta:
        model = RegistrarFruta
        fields = ["nombre", "variedad", "areacultivo", "produccionmes", "tipoterreno", "msnm", "temperatura"]

    def clean_email(self):
        nombre = self.cleaned_data.get("nombre")
        return nombre

#Formulario registrar finca
class RegistradoFruta(forms.ModelForm):
     class Meta:
        model = RegistrarFinca
        fields = ["nombre", "municipio", "departamento", "descripcion"]

