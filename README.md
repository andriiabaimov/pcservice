# PC Service
A Django app for service centers served with nginx and uWSGI


## Quick start

If you have no PostgreSQL running, the easiest way for you will be:
> docker run --name pcservice_db -p 5432:5432 -d postgres

If you have no idea how and where to deploy the app, the easiest way for you will be:
> docker run --link pcservice_db --name pcservice -p 80:80 -d andriiabaimov/pcservice

After both app and PostgreSQL are ready, run the migrations:
> docker exec -i pcservice python manage.py migrate

Collect static files (this stage also generates unique secret key for Django):
> docker exec -i pcservice python manage.py collectstatic --no-input

Finally, create superuser:
> echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'password')" | docker exec -i pcservice python manage.py shell
