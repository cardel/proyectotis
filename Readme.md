#Proyecto del curso tendencias Febrero - Junio 2016

##Ramas
* Master. Funciona en local 

##Aplicaciones

* <b>productortenant:</b> Es para registrar un tenant
* <b>gestionfruta:</b> Todo lo relativo a gestionar fruta

##Recomendaciones

<b>Base de datos</b>
* Postgres 9.4 o 9.6
* Usuario: tendencias
* Password: tendencias

 <b>Dependencias</b>

##Del sistema

* Python 3.5 o 3.6
* Servidor apache

###Del entorno

* virtualenv proyecto -p python3
* source proyecto/bin/activate
* pip install Django==2.0.4
* pip install django-bootstrap3==9.1.0
* pip install django-tenants==2.0.0
* pip install psycopg2==2.7.4
* pip install Pillow==4.0.0

#Crear SuperUsuario

python manage.py createsuperuser --username admin --email admin@admin.com

##Configurar

* python manage.py makemigrations gestionfruta
* python manage.py makemigrations productortenant
* python manage.py migrate_schemas --shared
* python manage.py migrate_schemas
* python manage.py migrate

##Poner en funcionamiento

* Ejecutar python manage.py.shell y escribir

...
from productortenant.models import Domain,Productor

nuevoproducto = Productor(tipo_documento = 1,identificacion = 1234,nombre = 'Public',fecha_nacimiento =  '2000-01-01',telefono = 000000,correo = 'admin@proyectotis.com',fecha_creacion = '2000-01-01', schema_name='public')

nuevoproducto.save()
query=Productor.objects.get(schema_name="public")


dominio_tenant = Domain(domain='localhost',is_primary=True, tenant_id=query.id)
dominio_tenant.save()
...

* Crear superusuario

...
python manage.py createsuperuser
...

Este usuario tendrá acceso a todo. Luego ejecutar

* python manage.py runserver localhost:8080



##Visualizar
  
En un navegador ingrese la dirección:

http://localhost:8080
 
