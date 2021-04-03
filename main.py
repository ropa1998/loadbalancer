import grpc
import yaml
from flask import Flask, request

# Init app
from service.geo_service_client import GeoServiceClient

app = Flask(__name__)

yamlfile = open("config.yaml", "r")

yaml_info = yaml.load(yamlfile, Loader=yaml.FullLoader)

geoservices_addresses_string = yaml_info["geoservices"]


def create_channel(address):
    return grpc.insecure_channel(address)


geoservices_channels = list(map(create_channel, geoservices_addresses_string))

geoservices_addresses = GeoServiceClient(geoservices_channels)


@app.route('/api/countries', methods=['GET'])
def get_countries():
    return {"countries": geoservices_addresses.get_countries()}


@app.route('/api/states', methods=['GET'])
def get_states():
    content = request.get_json()
    return {"states": geoservices_addresses.get_states(content["country"])}


@app.route('/api/cities', methods=['GET'])
def get_cities():
    content = request.get_json()
    return {"cities": geoservices_addresses.get_cities(content["state"])}


@app.route('/api/location-for-ip', methods=['GET'])
def get_location_for_id():
    content = request.get_json()
    return {"location": geoservices_addresses.get_location_for_ip(content["ip"])}


# A method that runs the application server.
if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=False, threaded=True, port=5000)
