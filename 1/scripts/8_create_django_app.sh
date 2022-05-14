cd ../

source env/bin/activate


django-admin startapp my_app

python manage.py makemigrations

python manage.py migrate


sh