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
* sudo apt-get install python3-pillow
* sudo apt-get install python-django
* sudo apt-get install postgresql
* sudo apt-get install postgresql-server-dev-all
* sudo pip3 install django-tenants --upgrade
* sudo pip3 install django-bootstrap3 --upgrade
* sudo pip3 install psycopg --upgrade

##Crear SuperUsuario

python3 manage.py createsuperuser --username admin --email admin@admin.com

##Poner a funcionar

python3 manage.py makemigrations gestionfruta
python3 manage.py makemigrations productotenant
python3 manage.py migrate_schemas
python3 manage.py migrate
python3 manage.py runserver localhost:8080

##Visualizar

En un navegador ingrese la dirección:

http://localhost:8080
