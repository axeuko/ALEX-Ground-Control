from alexpackages import ALEXSERVER
from flask import render_template, Response, redirect, request
import numpy as np
import cv2
import serial
import time
import freenect

def gen_frames():
    while True:
        frame, success = freenect.sync_get_video()
        frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()
            yield(b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@ALEXSERVER.route("/")
def landingpage():
    return render_template("public/ALEXGROUNDCONTROL.html")


@ALEXSERVER.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
