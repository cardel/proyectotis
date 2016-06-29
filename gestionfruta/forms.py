from django import forms
from django.forms.widgets  import FileInput, Textarea
from .models import Contacto, Fruta, Finca


#Formulario de registrar producto
class RegistrarFincaForm(forms.ModelForm):
    class Meta:
        model = Finca
        fields = '__all__'

    departament_choices = (
        ('Bogota', 'Bogota'),
        ('Valle', 'Valle'),
        ('Antioquia', 'Antioquia'),
        ('Cauca', 'Cauca'),
        ('Santander', 'Santander'),
        ('Guajira', 'Guajira'),
        ('Amazonas', 'Amazonas'),
        ('Huila', 'Huila'),
        ('Putumayo', 'Putumayo'),
    )

    nombre = forms.CharField(label="Nombre de la finca", max_length=120)

    departamento = forms.ChoiceField(
        label="Departamento",
        choices=departament_choices,
        required=False
    )

    municipio = forms.CharField(label="Municipio", max_length=120, required=True)
    imagen = forms.ImageField(label="Foto de la finca (500px por 500px preferiblemente)", widget=FileInput, required=True)
    descripcion = forms.CharField(label="Descripción", widget=Textarea, required=True)


#Formulario registrar finca
class RegistrarFrutaForm(forms.ModelForm):
    class Meta:
        model = Fruta
        fields = '__all__'

    nombre = forms.CharField(label="Nombre fruta", max_length=120,)
    variedad = forms.CharField(label="Variedad fruta", max_length=120, required=True)
    areacultivo = forms.CharField(label="Area cultivo fruta",max_length=20, required=True)
    produccionmes = forms.IntegerField(label="Producción mensual",required=True)
    tipoterreno = forms.CharField(label="Tipo terreno",max_length=120, required=True)
    msnm = forms.IntegerField(label="Altura Producción", required=True)
    temperatura = forms.IntegerField(label="Temperatura Producción", required=True)
    imagen = forms.ImageField(label="Imagen fruta",widget=FileInput, required=True)


class RegistrarContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

    direccion = forms.CharField(label="Dirección", max_length=120,required=True)
    telefono = forms.CharField(label="Teléfono", max_length=120, required=True)
    email = forms.EmailField(label="Correo electrónico", max_length=120, required=True)
