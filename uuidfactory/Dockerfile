FROM python:2.7-onbuild
MAINTAINER Thomas Maurice <thomas@maurice.fr>

EXPOSE 8000

CMD gunicorn --chdir /usr/src/app -b 0.0.0.0:8000 --access-logfile /dev/stdout --error-logfile /dev/stdout api:app
