import grpc
import yaml
from flask import Flask, request
import etcd3

# Init app
from service.auth_service_client import AuthServiceClient, constants
from service.geo_service_client import GeoServiceClient
from service.stock_service_client import StockServiceClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# client = etcd3.client(host='my-etcd', port=2379)
#
# auth_route = '/services/auth'
# geo_route = '/services/geo'
# stock_route = '/services/stock'
#
#
# def solve_auth_changes(event):
#     global auth_addresses
#
#     if isinstance(event.events[0], etcd3.events.DeleteEvent):
#         auth_nodes_map.pop(event.events[0].key.decode("utf-8"))
#
#         new_channels = list(map(create_channel, list(auth_nodes_map.values())))
#
#         auth_addresses = AuthServiceClient(new_channels)
#
#     if isinstance(event.events[0], etcd3.events.PutEvent):
#         if auth_nodes_map.get(event.events[0].key.decode("utf-8")) == event.events[0].value.decode("utf-8"):
#             return
#
#         auth_nodes_map[event.events[0].key.decode("utf-8")] = event.events[0].value.decode("utf-8")
#
#         new_channels = list(map(create_channel, list(auth_nodes_map.values())))
#
#         auth_addresses = AuthServiceClient(new_channels)
#
#
# def solve_geo_changes(event):
#     global geoservices_addresses
#
#     if isinstance(event.events[0], etcd3.events.DeleteEvent):
#         geo_nodes_map.pop(event.events[0].key.decode("utf-8"))
#
#         new_channels = list(map(create_channel, list(geo_nodes_map.values())))
#
#         geoservices_addresses = GeoServiceClient(new_channels)
#
#     if isinstance(event.events[0], etcd3.events.PutEvent):
#         if geo_nodes_map.get(event.events[0].key.decode("utf-8")) == event.events[0].value.decode("utf-8"):
#             return
#
#         geo_nodes_map[event.events[0].key.decode("utf-8")] = event.events[0].value.decode("utf-8")
#
#         new_channels = list(map(create_channel, list(geo_nodes_map.values())))
#
#         geoservices_addresses = GeoServiceClient(new_channels)
#
#
# def solve_stock_changes(event):
#     global stockservices_addresses
#
#     if isinstance(event.events[0], etcd3.events.DeleteEvent):
#         stock_nodes_map.pop(event.events[0].key.decode("utf-8"))
#
#         new_channels = list(map(create_channel, list(stock_nodes_map.values())))
#
#         stockservices_addresses = StockServiceClient(new_channels)
#
#     if isinstance(event.events[0], etcd3.events.PutEvent):
#         if stock_nodes_map.get(event.events[0].key.decode("utf-8")) == event.events[0].value.decode("utf-8"):
#             return
#
#         stock_nodes_map[event.events[0].key.decode("utf-8")] = event.events[0].value.decode("utf-8")
#
#         new_channels = list(map(create_channel, list(stock_nodes_map.values())))
#
#         stockservices_addresses = StockServiceClient(new_channels)
#
#
# client.add_watch_prefix_callback(auth_route, solve_auth_changes)
# client.add_watch_prefix_callback(geo_route, solve_geo_changes)
# client.add_watch_prefix_callback(stock_route, solve_stock_changes)
#
# auth_nodes_map = dict()
# geo_nodes_map = dict()
# stock_nodes_map = dict()


# def get_stockservices_adresses():
#     values = client.get_prefix(stock_route)
#     for value, x in values:
#         yield value.decode("utf-8")
#
#
# def get_geoservices_adresses():
#     values = client.get_prefix(geo_route)
#     for value, x in values:
#         yield value.decode("utf-8")
#
#
# def get_authservices_addresses():
#     values = client.get_prefix(auth_route)
#     for value, x in values:
#         auth_nodes_map[x.key.decode("utf-8")] = value.decode("utf-8")
#         yield value.decode("utf-8")

yamlfile = open("config/loadbalancer-config.yaml", "r")

yaml_info = yaml.load(yamlfile, Loader=yaml.FullLoader)

geoservices_addresses_string = yaml_info["geoservices"]

stockservices_addresses_string = yaml_info["stockservices"]

auth_addresses_string = yaml_info["authservices"]


def create_channel(address):
    return grpc.insecure_channel(address)


geoservices_channels = list(map(create_channel, geoservices_addresses_string))

geoservices_addresses = GeoServiceClient(geoservices_channels)

stockservices_channels = list(map(create_channel, stockservices_addresses_string))

stockservices_addresses = StockServiceClient(stockservices_channels)

auth_channels = list(map(create_channel, auth_addresses_string))

auth_addresses = AuthServiceClient(auth_channels)


@app.route('/api/products', methods=['POST'])
def get_products():
    content = request.get_json()
    response = authenticate(content)
    if response['status'] == constants['authenticated']:
        return {"products": stockservices_addresses.get_products_from_country(content["country"]), "country": content["country"]}
    return {"error": "Not-authenticated"}


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
    app.run(debug=False, threaded=True, host='0.0.0.0', port=5000)
    print("Hello World!")
