# PC Service
A Django app for service centers served with nginx and uWSGI


## Quick start

If you have no PostgreSQL running, the easiest way for you is to run docker container with it:
> docker run --name pcservice_db -p 5432:5432 -d postgres

If you have no idea how and where to deploy the app, the easiest way for you is to run docker container wit it:
> docker run --link pcservice_db --name pcservice -p 80:80 -d andriiabaimov/pcservice

Run the migrations:
> docker exec -i pcservice python manage.py migrate

Create superuser:
> echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'password')" | docker exec -i pcservice python manage.py shell