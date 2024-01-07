#!usr/bin/python3

from flask import Flask, Blueprint, jsonify, make_response
from flask_restful import Api
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)

host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)


@app.teardown_appcontext
def teardown_appcontext(error):
    """Closes storage"""
    storage.close()


if __name__ == "__main__":
    """main function"""
    app.run(host=host, port=port, threaded=True)
