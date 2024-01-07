#!/usr/bin/python3

import os
from flask import Flask, jsonify
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
    
@app.errorhandler(404)
def page_not_found(e):
    """404 page"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    """main function"""
    app.run(host=host, port=port, threaded=True)
