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
    tipo_documento = forms.ChoiceField( choices=document_choices, label="Tipo documento")
    identificacion = forms.CharField(max_length=100, label="Número documento")
    schema_name = forms.CharField(max_length=100, label="Dirección de su sitio")
    nombre = forms.CharField(max_length=100, label="Nombre completo")
    fecha_nacimiento =  forms.DateField(widget=SelectDateWidget,label="Fecha nacimiento")
    telefono = forms.CharField(max_length=100,label="Teléfono")
    correo = forms.EmailField(label="Correo electrónico")





