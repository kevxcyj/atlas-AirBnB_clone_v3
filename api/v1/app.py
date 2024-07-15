#!/usr/bin/python3
""" This is used to connect to the API """

from flask import Flask, Blueprint
from models import storage
from api.v1.views import app_views
import os

host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = int(os.getenv('HBNB_API_PORT', '5000'))

app = Flask(__name__)
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

@app.teardown_appcontext
def close_storage(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)