# -*- coding: utf-8 -*-

from cStringIO import StringIO

import faceswap
from flask import Flask
from flask import request
from flask import send_file
import requests
import tempfile


app = Flask(__name__, static_folder='/srv/static')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the files
        if request.form.has_key('head_url'):
            head_image = get_image_from_url(request.form.get('head_url'))
        elif request.files.has_key('head_upload'):
            head_image = request.files.get('head_upload')
        else:
            complain("No head image")

        if request.form.has_key('face_url'):
            face_image = get_image_from_url(request.form.get('face_url'))
        elif request.files.has_key('face_upload'):
            face_image = request.files.get('face_upload')
        else:
            complain("No face image")

        # Do the merge
        merged_image = faceswap.merge_images(head_image, face_image)
        return send_file(
            StringIO(merged_image),
            attachment_filename="test.jpg",
            as_attachment=False
        )

    else:
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
