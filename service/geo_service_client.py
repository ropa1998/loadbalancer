# open a gRPC channel
import yaml
from retrying import retry

import geoService_pb2
import geoService_pb2_grpc
from load_balancer.RoundRobinBalancer import RoundRobinBalancer

yamlfile = open("config.yaml", "r")
yaml_info = yaml.load(yamlfile, Loader=yaml.FullLoader)
max_retries = yaml_info["max_retries"]


class GeoServiceClient:

    def __init__(self, channels):
        self.balancer = RoundRobinBalancer(channels)

    @retry(stop_max_attempt_number=max_retries)
    def get_countries(self):
        stub = self.get_stub()
        empty = geoService_pb2.Empty()
        response = stub.GetAllCountries(empty)
        return list(response.countries)

    @retry(stop_max_attempt_number=max_retries)
    def get_states(self, country):
        stub = self.get_stub()
        country = geoService_pb2.Country(name=country)
        response = stub.GetSubCountries(country)
        return list(response.subCountries)

    @retry(stop_max_attempt_number=max_retries)
    def get_cities(self, state):
        stub = self.get_stub()
        country = geoService_pb2.SubCountry(name=state)
        response = stub.GetCities(country)
        return list(response.cities)

    @retry(stop_max_attempt_number=max_retries)
    def get_location_for_ip(self, ip):
        stub = self.get_stub()
        ip = geoService_pb2.Ip(direction=ip)
        response = stub.GetLocationOfIp(ip)
        return {"country": response.country, "state": response.state}

    def get_stub(self):
        channel = self.balancer.get_channel()
        stub = geoService_pb2_grpc.GeoServiceStub(channel)
        print("Using " + str(channel))
        return stub
