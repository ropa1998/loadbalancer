import grpc
from flask import Flask, request, jsonify
import sqlite3
import os

# Init app
from geo_service_client import GeoServiceClient

app = Flask(__name__)

channels = [grpc.insecure_channel('localhost:50051'),
            grpc.insecure_channel('localhost:50052'),
            grpc.insecure_channel('localhost:50057')]

geoservice = GeoServiceClient(channels)


@app.route('/api/countries', methods=['GET'])
def get_countries():
    return {"countries": geoservice.get_countries()}


@app.route('/api/states', methods=['GET'])
def get_states():
    content = request.get_json()
    return {"states": geoservice.get_states(content["country"])}


@app.route('/api/cities', methods=['GET'])
def get_cities():
    content = request.get_json()
    return {"cities": geoservice.get_cities(content["state"])}


@app.route('/api/location-for-id', methods=['GET'])
def get_location_for_id():
    content = request.get_json()
    return {"location": geoservice.get_location_for_ip(content["ip"])}


# A method that runs the application server.
if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=False, threaded=True, port=5000)
