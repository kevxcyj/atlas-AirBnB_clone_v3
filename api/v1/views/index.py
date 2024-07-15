#!/usr/bin/python3
""" Retuns status for app_views """

from flask import jsonify
from models import storage
from . import app_views

@app_views.route('/status', strict_slashes=False)
def status():
    return jsonify({"status": "OK"})