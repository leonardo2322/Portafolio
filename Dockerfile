FROM python:3.11-alpine3.20

WORKDIR /web

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir -r /web/requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Portafolio.wsgi:application"]