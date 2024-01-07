#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """
    function for status route that returns the status
    """
    if request.method == 'GET':
        resp = {"status": "OK"}
        return jsonify(resp)
    
@app_views.route('/stats', methods=['GET'])
def stats():
    """
    function for stats route that returns the stats
    """
    if request.method == 'GET':
        classes = {"amenities": "Amenity", "cities": "City", "places": "Place",
                   "reviews": "Review", "states": "State", "users": "User"}
        resp = {}
        for key, value in classes.items():
            resp[key] = storage.count(value)
        return jsonify(resp)
