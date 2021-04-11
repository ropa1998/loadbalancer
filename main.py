import grpc
import yaml
from flask import Flask, request

# Init app
from service.auth_service_client import AuthServiceClient, constants
from service.geo_service_client import GeoServiceClient

app = Flask(__name__)


def get_yaml():
    yamlfile = open("config.yaml", "r")
    return yaml.load(yamlfile, Loader=yaml.FullLoader)


def get_geoservices_adresses():
    yaml_info = get_yaml()
    return yaml_info["geoservices"]


def get_authservices_addresses():
    yaml_info = get_yaml()
    return yaml_info["authservices"]


geoservices_addresses_string = get_geoservices_adresses()

auth_addresses_string = get_authservices_addresses()


def create_channel(address):
    return grpc.insecure_channel(address)


geoservices_channels = list(map(create_channel, geoservices_addresses_string))

geoservices_addresses = GeoServiceClient(geoservices_channels)

auth_channels = list(map(create_channel, auth_addresses_string))

auth_addresses = AuthServiceClient(auth_channels)


@app.route('/api/countries', methods=['POST'])
def get_countries():
    content = request.get_json()
    response = authenticate(content)
    if response['status'] == constants['authenticated']:
        return {"countries": geoservices_addresses.get_countries()}
    return {"error": "Not-authenticated"}


@app.route('/api/states', methods=['POST'])
def get_states():
    content = request.get_json()
    response = authenticate(content)
    if response['status'] == constants['authenticated']:
        return {"states": geoservices_addresses.get_states(content["country"])}
    return {"error": "Not-authenticated"}


@app.route('/api/cities', methods=['POST'])
def get_cities():
    content = request.get_json()
    response = authenticate(content)
    if response['status'] == constants['authenticated']:
        return {"cities": geoservices_addresses.get_cities(content["state"])}
    return {"error": "Not-authenticated"}


@app.route('/api/location-for-ip', methods=['POST'])
def get_location_for_id():
    content = request.get_json()
    response = authenticate(content)
    if response['status'] == constants['authenticated']:
        return {"location": geoservices_addresses.get_location_for_ip(content["ip"])}
    return {"error": "Not-authenticated"}


def authenticate(content):
    return {"status": auth_addresses.authenticate(email=content["email"], password=content["password"])}


# A method that runs the application server.
if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=False, threaded=True, port=5000)
