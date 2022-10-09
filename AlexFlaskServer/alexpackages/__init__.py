from flask import Flask


ALEXSERVER = Flask(__name__)

from alexpackages import views
from alexpackages import motion
