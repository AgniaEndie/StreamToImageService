import cv2
from flask import *
import requests

app = Flask(__name__)


@app.route('/camera/<id>')
def stream_to_image(id):
    # test23
    cameras = requests.get('http://camera-registry-service:80/get/all').json()
    for camera in cameras:
        if camera[0] == id:
            localCamera = cv2.VideoCapture(camera[0])
            success, frame = localCamera.read()

            return Response(frame, mimetype='multipart/x-mixed-replace; boundary=frame')
        else:
            return Response("", 500)


app.run("0.0.0.0", port=8080, debug=True)
