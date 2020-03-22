FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
RUN apk add --no-cache libressl-dev musl-dev libffi-dev
RUN apk add gcc musl-dev python3-dev
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./flaskr/static/ /var/www/app/static
COPY . /app
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install requests
RUN pip install urllib3
RUN pip install python-dateutil
