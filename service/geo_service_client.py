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
        for i in range(0, 100):
            while True:
                try:
                    stub = self.get_stub()
                    empty = geoService_pb2.Empty()
                    response = stub.GetAllCountries(empty)
                    return list(response.countries)
                except Exception:
                    continue
                break

    def get_states(self, country):
        for i in range(0, 100):
            while True:
                try:
                    stub = self.get_stub()
                    country = geoService_pb2.Country(name=country)
                    response = stub.GetSubCountries(country)
                    return list(response.subCountries)
                except Exception:
                    continue
                break

    def get_cities(self, state):
        for i in range(0, 100):
            while True:
                try:
                    stub = self.get_stub()
                    country = geoService_pb2.SubCountry(name=state)
                    response = stub.GetCities(country)
                    return list(response.cities)
                except Exception:
                    continue
                break

    def get_location_for_ip(self, ip):
        for i in range(0, 100):
            while True:
                try:
                    stub = self.get_stub()
                    ip = geoService_pb2.Ip(direction=ip)
                    response = stub.GetLocationOfIp(ip)
                    return {"country": response.country, "state": response.state}
                except Exception:
                    continue
                break

    def get_stub(self):
        channel = self.balancer.get_channel()
        stub = geoService_pb2_grpc.GeoServiceStub(channel)
        print("Using " + str(channel))
        return stub
