# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__, static_folder='/srv/static')
from facemash import views
