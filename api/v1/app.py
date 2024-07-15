#!/usr/bin/python3
""" This is used to connect to the API """

from flask import Flask, Blueprint
from models import storage
import os

app = Flask(__name__)
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

@app.teardown_appcontext
def close_storage(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)