from flask import *
import requests

app = Flask(__name__)


@app.route('/camera/<id>')
def stream_to_image(id):
    #test
    cameras = requests.get('http://camera-registry-service/get/all').json()
    for camera in cameras:
        if camera["uuid"] == id:
            return requests.get(camera['external_ip'])
        else:
            return Response("", 500)
