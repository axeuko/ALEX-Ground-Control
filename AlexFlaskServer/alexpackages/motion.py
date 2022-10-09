from alexpackages import ALEXSERVER
from flask import render_template, Response, redirect, request
import serial
import time
import freenect

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)

@ALEXSERVER.route('/forward')
def forward():
    arduino.write(bytes('F', 'utf-8'))
    return ('', 204)

@ALEXSERVER.route('/backward')
def backward():
    arduino.write(bytes('B', 'utf-8'))
    return ('', 204)

@ALEXSERVER.route('/left')
def left():
    arduino.write(bytes('L', 'utf-8'))
    return ('', 204)

@ALEXSERVER.route('/right')
def right():
    arduino.write(bytes('R', 'utf-8'))
    return ('', 204)
    
@ALEXSERVER.route('/stop')
def stop():
    arduino.write(bytes('M', 'utf-8'))
    return ('', 204)

@ALEXSERVER.route('/speedup')
def speed_up():
    arduino.write(bytes('1', 'utf-8'))
    return ('', 204)

@ALEXSERVER.route('/slowdown')
def slow_down():
    arduino.write(bytes('2', 'utf-8'))
    return ('', 204)
