#comment pour test 2
FROM python:3.10-slim-buster

WORKDIR /Python_P13

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SENTRY_DSN $SENTRY_DSN



RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput --clear

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000
