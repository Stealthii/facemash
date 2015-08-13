# -*- coding: utf-8 -*-

from cStringIO import StringIO

import faceswap
from flask import request
from flask import send_file
import requests
import tempfile


from facemash import app


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
    return send_file(
        StringIO(merged_image),
        attachment_filename="test.jpg",
        as_attachment=False
    )


@app.route('/', methods=['GET'])
def index():
    # Show merge form
    return app.send_static_file('index.html')


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
