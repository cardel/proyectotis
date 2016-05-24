from django import forms
from .models import Registrado


class RegistradoForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre", "variedad", "areacultivo", "produccionmes", "tipoterreno", "msnm", "temperatura"]

    def clean_email(self):
        nombre = self.cleaned_data.get("nombre")
        return nombre


