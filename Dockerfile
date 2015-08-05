FROM debian:jessie

RUN (apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y python python-dev python-pip nginx sqlite3 supervisor uwsgi)

# install our code
ADD app /opt/flask/app
ADD static /srv/static
RUN mkdir /srv/media

# setup all the configfiles
run echo "daemon off;" >> /etc/nginx/nginx.conf
run rm /etc/nginx/sites-enabled/default
run ln -s /opt/flask/nginx-app.conf /etc/nginx/sites-enabled/
run ln -s /opt/flask/supervisor-app.conf /etc/supervisor/conf.d/

# run pip install
run pip install -r /opt/flask/app/requirements.txt

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

expose 80
cmd ["supervisord", "-n"]
