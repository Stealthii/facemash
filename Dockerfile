FROM debian:jessie

RUN (apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y python python-dev python-pip nginx sqlite3 supervisor uwsgi uwsgi-plugin-python)

# install our code
ADD app /opt/flask/app
ADD static /srv/static
RUN mkdir /srv/media

# setup all the configfiles
ADD ./supervisord.conf /etc/supervisord.conf
ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./uwsgi.ini /etc/uwsgi.ini
ADD ./uwsgi_params /opt/flask/uwsgi_params

# run pip install
run pip install -r /opt/flask/app/requirements.txt

# restart nginx to load the config
RUN service nginx stop

expose 80
CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]
