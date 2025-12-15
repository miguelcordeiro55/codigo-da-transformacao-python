django-admin startproject core
cd core
python manage.py startapp produtos

INSTALLED_APPS = [
    ...
    'produtos',
]

python manage.py makemigrations
python manage.py migrate
