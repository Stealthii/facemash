FROM debian:jessie

RUN (apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y python python-dev python-setuptools nginx sqlite3 supervisor)
RUN (easy_install pip &&\
  pip install uwsgi)

# install our code
add . /opt/flask/

# setup all the configfiles
run echo "daemon off;" >> /etc/nginx/nginx.conf
run rm /etc/nginx/sites-enabled/default
run ln -s /opt/flask/nginx-app.conf /etc/nginx/sites-enabled/
run ln -s /opt/flask/supervisor-app.conf /etc/supervisor/conf.d/

# run pip install
run pip install -r /opt/flask/app/requirements.txt

expose 80
cmd ["supervisord", "-n"]
