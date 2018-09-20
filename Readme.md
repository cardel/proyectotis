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
* pip install -r requerimientos.txt

El archivo requerimientos.txt está en el raiz del proyecto



##Configurar

* python manage.py makemigrations
* python manage.py migrate_schemas --shared

##Poner en funcionamiento

* python manage.py shell

Escribir linea por linea:

```
from productortenant.models import Domain,Productor

nuevoproducto = Productor(tipo_documento = 1,identificacion = 1234,nombre = 'Public',fecha_nacimiento =  '2000-01-01',telefono = 000000,correo = 'admin@proyectotis.com',fecha_creacion = '2000-01-01', schema_name='public')

nuevoproducto.save()
query=Productor.objects.get(schema_name="public")


dominio_tenant = Domain(domain='localhost',is_primary=True, tenant_id=query.id)
dominio_tenant.save()

exit()
```

#Crear SuperUsuario
```
python manage.py createsuperuser --username admin --email admin@admin.com
```

Este usuario tendrá acceso a todo. Luego ejecutar

* python manage.py runserver localhost:8080



##Visualizar
  
En un navegador ingrese la dirección:

http://localhost:8080
 
