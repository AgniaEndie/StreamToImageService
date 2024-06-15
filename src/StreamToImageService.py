from flask import *
import requests

app = Flask(__name__)


@app.route('/camera/<id>')
def stream_to_image(id):
    # test23
    cameras = requests.get('http://camera-registry-service:80/get/all').json()
    for camera in cameras:
        if camera[0] == id:
            return requests.get(camera[1],stream=True)
        else:
            return Response("", 500)


app.run("0.0.0.0", port=8080, debug=True)
