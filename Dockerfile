FROM debian:jessie

# install dependencies from apt
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y cmake curl libboost-python-dev python python-dev python-opencv python-pil python-pip nginx sqlite3 supervisor uwsgi uwsgi-plugin-python && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# download, unpack, compile and install dlib
RUN cd /tmp && curl http://dlib.net/files/dlib-18.16.tar.bz2 | tar xj && \
    cd /tmp/dlib-18.16/python_examples && ./compile_dlib_python_module.bat && \
    cp ./build/dlib.so /usr/local/lib/python2.7/dist-packages/ && \
    rm -rf /tmp/* /var/tmp/*

# download and unpack trained model from sourceforge
RUN mkdir -p /models && curl http://netcologne.dl.sourceforge.net/project/dclib/dlib/v18.10/shape_predictor_68_face_landmarks.dat.bz2 | bunzip2 -c > /models/shape_predictor_68_face_landmarks.dat

# setup all the configfiles
ADD ./supervisord.conf /etc/supervisord.conf
ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./uwsgi.ini /etc/uwsgi.ini
ADD ./uwsgi_params /opt/flask/uwsgi_params

# restart nginx to load the config
RUN service nginx stop

# install our code
ADD app /opt/flask/app
ADD static /srv/static
RUN mkdir /srv/media

# run pip install
run pip install -r /opt/flask/app/requirements.txt

expose 80
CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]
