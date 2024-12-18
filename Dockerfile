
FROM python:3.11-alpine3.20


WORKDIR /web


COPY ./requirements.txt /web/requirements.txt


RUN apk update && apk add --no-cache \
    libpq-dev gcc musl-dev bash \
    && rm -rf /var/cache/apk/*

RUN pip install --no-cache-dir -r /web/requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
COPY ./wait-for-it.sh /wait-for-it.sh

RUN chmod +x /entrypoint.sh /wait-for-it.sh


RUN mkdir -p /web/static /web/media

COPY . /web

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
