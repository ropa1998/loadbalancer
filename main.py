import grpc
import yaml
from flask import Flask, request
import etcd3

# Init app
from service.auth_service_client import AuthServiceClient, constants
from service.geo_service_client import GeoServiceClient

app = Flask(__name__)

client = etcd3.client(host='127.0.0.1', port=2379)

auth_route = '/services/auth'
geo_route = '/services/geo'


def solve_auth_changes(event):
    global auth_addresses

    if isinstance(event.events[0], etcd3.events.DeleteEvent):
        auth_nodes_map.pop(event.events[0].key.decode("utf-8"))

        new_channels = list(map(create_channel, list(auth_nodes_map.values())))

        auth_addresses = AuthServiceClient(new_channels)

    if isinstance(event.events[0], etcd3.events.PutEvent):
        if auth_nodes_map.get(event.events[0].key.decode("utf-8")) == event.events[0].value.decode("utf-8"):
            return

        auth_nodes_map[event.events[0].key.decode("utf-8")] = event.events[0].value.decode("utf-8")

        new_channels = list(map(create_channel, list(auth_nodes_map.values())))

        auth_addresses = AuthServiceClient(new_channels)


def solve_geo_changes(event):
    global geoservices_addresses

    if isinstance(event.events[0], etcd3.events.DeleteEvent):
        geo_nodes_map.pop(event.events[0].key.decode("utf-8"))

        new_channels = list(map(create_channel, list(geo_nodes_map.values())))

        geoservices_addresses = GeoServiceClient(new_channels)

    if isinstance(event.events[0], etcd3.events.PutEvent):
        if geo_nodes_map.get(event.events[0].key.decode("utf-8")) == event.events[0].value.decode("utf-8"):
            return

        geo_nodes_map[event.events[0].key.decode("utf-8")] = event.events[0].value.decode("utf-8")

        new_channels = list(map(create_channel, list(geo_nodes_map.values())))

        geoservices_addresses = GeoServiceClient(new_channels)


client.add_watch_prefix_callback(auth_route, solve_auth_changes)
client.add_watch_prefix_callback(geo_route, solve_geo_changes)

auth_nodes_map = dict()
geo_nodes_map = dict()


def get_geoservices_adresses():
    values = client.get_prefix(geo_route)
    for value, x in values:
        yield value.decode("utf-8")


def get_authservices_addresses():
    values = client.get_prefix(auth_route)
    for value, x in values:
        auth_nodes_map[x.key.decode("utf-8")] = value.decode("utf-8")
        yield value.decode("utf-8")


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
