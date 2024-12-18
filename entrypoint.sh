#!/bin/sh


./wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Database is up - continuing..."


python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py makemigrations Home
python manage.py migrate Home
exec gunicorn --bind 0.0.0.0:8000 Portafolio.wsgi:application




