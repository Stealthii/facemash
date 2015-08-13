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
    if request.form.has_key('head-url'):
        head_image = get_image_from_url(request.form.get('head-url'))
    elif request.files.has_key('head-file'):
        print "We got a head"
        head_image = request.files.get('head-file')
        print "head assigned"
        if not head_image:
            print "definitely"
    else:
        complain("No head image")

    if request.form.has_key('face-url'):
        face_image = get_image_from_url(request.form.get('face-url'))
    elif request.files.has_key('face-file'):
        print "We got a face"
        face_image = request.files.get('face-file')
        print "Face assigned"
        if not face_image:
            print "definitely"
    else:
        complain("No face image")

    if not head_image:
        print "what the fuck, where head gone?"

    # Do the merge
    merged_image = faceswap.merge_images(head_image, face_image)
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
