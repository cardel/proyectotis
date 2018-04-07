#Proyecto del curso tendencias Febrero - Junio 2016

##Ramas
- Master. Funciona en local 
- Cardel: Funciona en servidores Amazon

##Aplicaciones

- <b>productortenant:</b> Es para registrar un tenant
- <b>gestionfruta:</b> Todo lo relativo a gestionar fruta

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
* sudo pip3 install django-tenants
* sudo pip3 install django-bootstrap3

##Crear SuperUsuario

python3 manage.py createsuperuser --username admin --email admin@admin.com

##Poner a funcionar

python3 manage.py makemigrations
python3 manage.py migrate_schemas
python3 manage.py migrate
