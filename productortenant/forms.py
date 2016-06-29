from django import forms
from django.forms.extras.widgets import SelectDateWidget
from productortenant.models import Productor

class CrearProductorForm(forms.ModelForm):

    class Meta:
        model = Productor
        fields = '__all__'

    document_choices = (
        ('CC', 'Cédula'),
        ('NIT', 'NIT'),
        ('OTHER', 'Otro'),
    )
    tipo_documento = forms.ChoiceField( choices=document_choices, label="Tipo documento", required=True)
    identificacion = forms.CharField(max_length=100, label="Número documento", required=True)
    schema_name = forms.CharField(max_length=100, label="Dirección de su sitio", required=True)
    nombre = forms.CharField(max_length=100, label="Nombre completo", required=True)
    fecha_nacimiento =  forms.DateField(widget=SelectDateWidget,label="Fecha nacimiento", required=True)
    telefono = forms.CharField(max_length=100,label="Teléfono", required=True)
    
    usuario = forms.CharField(label="Usuario", required=True)
    password = forms.CharField(label="Contraseña", min_length=8, widget=forms.PasswordInput, required=True)




