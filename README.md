## Just forked from [https://github.com/dockerfiles/django-uwsgi-nginx](https://github.com/dockerfiles/django-uwsgi-nginx), change Django to Flask.


# Flask, uWSGI and Nginx in a container

This Dockerfile allows you to build a Docker container with a fairly standard
and speedy setup for Flask with uWSGI and Nginx.

uWSGI from a number of benchmarks has shown to be the fastest server 
for python applications and allows lots of flexibility.

Nginx has become the standard for serving up web applications and has the 
additional benefit that it can talk to uWSGI using the uWSGI protocol, further
elinimating overhead. 

Most of this setup comes from the excellent tutorial on 
<del>https://uwsgi.readthedocs.org/en/latest/tutorials/Django_and_nginx.html</del>
[http://flask.pocoo.org/docs/deploying/uwsgi/#configuring-nginx](http://flask.pocoo.org/docs/deploying/uwsgi/#configuring-nginx)

Feel free to clone this and modify it to your liking. And feel free to 
contribute patches.

### Build and run
* docker build -t webapp .
* docker run -d webapp

### How to insert your application

In /app currently a flask project is created with startproject. Yowill
probably want to replace the content of /app with the root of your flask 
project.

uWSGI chdirs to /app so in uwsgi.ini you will need to make sure the python path
to the wsgi.py file is relative to that.

