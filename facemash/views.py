# -*- coding: utf-8 -*-

from facemash import app
from flask import render_template
from flask import request
import faceswap
import os
import requests
import tempfile
import time


@app.route('/upload', methods=['POST'])
def upload():
    # Get the files
    if not request.files['head-file'].filename == '':
        head_image = request.files['head-file']
    else:
        complain("No head image")
    if not request.files['face-file'].filename == '':
        face_image = request.files['face-file']
    else:
        complain("No face image")

    # Do the merge
    try:
        merged_image = faceswap.merge_images(head_image, face_image)
    except:
        raise

    filename = time.strftime("%Y%m%d-%H%M%S") + ".jpg"
    filepath = os.path.join("/srv/media", filename)
    servepath = os.path.join("/media", filename)
    with open(filepath, 'wb') as f:
        f.write(merged_image)

    return render_template('image.html', mashed_image=servepath)


@app.route('/', methods=['GET'])
def index():
    # Show merge form
    return app.send_static_file('index.html')


@app.route('/simple', methods=['GET'])
def simple_index():
    # Show merge form
    return app.send_static_file('simple_form.html')


def get_image_from_url(url):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        f = tempfile.TemporaryFile()
        for chunk in r.iter_content(1024):
            f.write(chunk)
        f.seek(0)
        return f
    return None


def complain(string):
    return string


def test():
    app.run(debug=True)

if __name__ == '__main__':
    test()
