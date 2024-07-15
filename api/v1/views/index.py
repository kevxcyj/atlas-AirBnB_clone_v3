#!/usr/bin/python3
""" Retuns status for app_views """

from flask import jsonify
from models import storage
from . import app_views

@app_views.route('/status', strict_slashes=False)
def status():
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def status_count():
    """ Endpoint that retrieves number of each objects """
    counts_status = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(counts_status)


if __name__ == "__main__":
    pass
