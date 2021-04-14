import grpc
import yaml
from flask import Flask, request
import etcd3

# Init app
from service.auth_service_client import AuthServiceClient, constants
from service.geo_service_client import GeoServiceClient

app = Flask(__name__)

client = etcd3.client(host='127.0.0.1', port=2379)


def get_geoservices_adresses():
    values = client.get_prefix('/services/geo')
    for value, x in values:
        yield value.decode("utf-8")


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


# lo que tengo que hacer ahora es primero levantar los que este publicados y crearlos
# despues tengo que armarme un watcher que sepa reaccionar al auth y al geo


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
