#Proyecto del curso tendencias Febrero - Junio 2016

##Ramas
* Master. Funciona en local 

##Aplicaciones

* <b>productortenant:</b> Es para registrar un tenant
* <b>gestionfruta:</b> Todo lo relativo a gestionar fruta

##Recomendaciones

<b>Base de datos</b>
* Postgres
* Usuario: tendencias
*  Password: tendencias

 <b>Dependencias</b>

##Del sistema

* Python 3.5 o 3.6
* Servidor apache
* Base de datos postgresSQL 9.4 o 9.6

##Bases de datos

* Usuario: multitenant
* Contraseña: multitenant
* Base de datos: multitenant

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

##Poner a funcionar

* python manage.py makemigrations gestionfruta
* python manage.py makemigrations productotenant
* python manage.py migrate_schemas
* python manage.py migrate
* python manage.py runserver localhost:8080
##Visualizar
  
En un navegador ingrese la dirección:

http://localhost:8080
 
