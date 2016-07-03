from django.views.generic import CreateView, TemplateView, UpdateView
from .models import  Finca, Fruta, Contacto
from django.db import connection

from django.core import serializers

# Create your views here.

from .forms import RegistrarFincaForm, RegistrarFrutaForm, RegistrarContactoForm

def parse_data(data, Model):

    result = []

    # flatten the dictionary
    def flatten_dict(d):
        """
        Because the only nested dict here is the fields, let's just
        remove the 'fields' suffix so that the fields can be loaded in
        template by name
        """
        def items():
            for key, value in d.items():
                if isinstance(value, dict):
                    for subkey, subvalue in flatten_dict(value).items():
                        yield subkey, subvalue
                else:
                    yield key, value

        return dict(items())

    for d in data:
        # change the 'pk' key name into its actual name in the database
        d[Model._meta.pk.name] = d.pop('pk')
        # append the flattend dict of each object's field-value to the result
        result.append(flatten_dict(d))

    return result


class Home(TemplateView):
    template_name = 'gestionfruta/inicio.html'

#Marca para indicar que se requiere estar logueado




class RegistrarFincaView(CreateView):
    template_name =  'gestionfruta/registrarFinca.html'
    form_class = RegistrarFincaForm
    success_url = "/adminfinca"


    def get_context_data(self, **kwargs):
        context = super(RegistrarFincaView, self).get_context_data(**kwargs)

        #Transformar a JSON
        finca = serializers.serialize("python", Finca.objects.all()[:1])

        #Parsear los datos

        contexto = {
            'finca' : parse_data(finca, Finca),
        }

        context.update(contexto)
        return context

    def form_valid(self, form):
        form.save()
        return super(RegistrarFincaView, self).form_valid(form)

class EditarFincaView(UpdateView):
    form_class = RegistrarFincaForm
    model = Finca
    success_url = "/adminfinca"
    template_name =  'gestionfruta/editarFinca.html'



class RegistrarFrutaView(CreateView):
    template_name =  'gestionfruta/registrarFruta.html'
    form_class = RegistrarFrutaForm
    success_url = "/adminfruta"




    def get_context_data(self, **kwargs):
        context = super(RegistrarFrutaView, self).get_context_data(**kwargs)
        #Transformar a JSON
        fruta = serializers.serialize("python", Fruta.objects.all())
        #Parsear los datos

        contexto = {
            'fruta' : parse_data(fruta, Fruta),
        }

        context.update(contexto)
        return context

class EditarFrutaView(UpdateView):
    model = Fruta
    template_name = 'gestionfruta/editarFruta.html'
    form_class = RegistrarFrutaForm
    success_url = "/adminfruta"




class AdminContactoView(CreateView):

    model = Contacto
    template_name = 'gestionfruta/admincontacto.html'
    form_class = RegistrarContactoForm
    success_url = "/adminContacto"

    def get_context_data(self, **kwargs):
        context = super(AdminContactoView, self).get_context_data(**kwargs)
        #Transformar a JSON
        contacto = serializers.serialize("python", Contacto.objects.all())
        #Parsear los datos

        contexto = {
            'contacto' : parse_data(contacto, Contacto),
        }

        context.update(contexto)
        return context

class EditarContactoView(UpdateView):
    model = Contacto
    template_name = 'gestionfruta/editarContacto.html'
    form_class = RegistrarContactoForm
    success_url = "/adminContacto"

class FincaView(TemplateView):
    template_name = 'gestionfruta/publicoFinca.html'

    def get_context_data(self, **kwargs):
        context = super(FincaView, self).get_context_data(**kwargs)

        #Transformar a JSON
        finca = serializers.serialize("python", Finca.objects.all()[:1])

        #Parsear los datos

        contexto = {
            'finca' : parse_data(finca, Finca),
        }

        context.update(contexto)
        return context

class FrutaView(TemplateView):
    template_name = 'gestionfruta/publicoFruta.html'

    def get_context_data(self, **kwargs):
        context = super(FrutaView, self).get_context_data(**kwargs)
        #Transformar a JSON
        fruta = serializers.serialize("python", Fruta.objects.all())
        #Parsear los datos

        contexto = {
            'fruta' : parse_data(fruta, Fruta),
        }

        context.update(contexto)
        return context

class ContactoView(TemplateView):
    template_name = 'gestionfruta/publicoContacto.html'

    def get_context_data(self, **kwargs):
        context = super(ContactoView, self).get_context_data(**kwargs)
        #Transformar a JSON
        contacto = serializers.serialize("python", Contacto.objects.all())
        #Parsear los datos

        contexto = {
            'contacto' : parse_data(contacto, Contacto),
        }

        context.update(contexto)
        return context