# open a gRPC channel
import logging

import grpc
import geoService_pb2
import geoService_pb2_grpc
from load_balancer.RoundRobinBalancer import RoundRobinBalancer


class GeoServiceClient:

    def __init__(self, channels):
        self.balancer = RoundRobinBalancer(channels)

    def get_countries(self):
        stub = self.get_stub()
        empty = geoService_pb2.Empty()
        response = stub.GetAllCountries(empty)
        return list(response.countries)

    def get_states(self, country):
        stub = self.get_stub()
        country = geoService_pb2.Country(name=country)
        response = stub.GetSubCountries(country)
        return list(response.subCountries)

    def get_cities(self, state):
        stub = self.get_stub()
        country = geoService_pb2.SubCountry(name=state)
        response = stub.GetSubCountries(country)
        return list(response.cities)

    def get_location_for_ip(self, ip):
        stub = self.get_stub()
        ip = geoService_pb2.Ip(ip=ip)
        response = stub.GetLocationOfIp(ip)
        return {"country": response.country, "state": response.state}

    def get_stub(self):
        channel = self.balancer.get_channel()
        stub = geoService_pb2_grpc.GeoServiceStub(channel)
        print("Using " + str(channel))
        return stub
