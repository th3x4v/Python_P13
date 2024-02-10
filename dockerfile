#comment pour test 2
FROM python:3.10-slim-buster

WORKDIR /Python_P13

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SENTRY_DSN https://22641b8aef8958ea73fe55efa050446f@o4506476129681408.ingest.sentry.io/4506605297532928


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput --clear

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000
