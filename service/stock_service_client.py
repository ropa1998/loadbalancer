# open a gRPC channel
import yaml
from retrying import retry

import stockService_pb2
import stockService_pb2_grpc

from load_balancer.RoundRobinBalancer import RoundRobinBalancer

yamlfile = open("config.yaml", "r")
yaml_info = yaml.load(yamlfile, Loader=yaml.FullLoader)
max_retries = yaml_info["max_retries"]


class StockServiceClient:

    def __init__(self, channels):
        self.balancer = RoundRobinBalancer(channels)

    @retry(stop_max_attempt_number=max_retries)
    def get_products_from_country(self, country):
        stub = self.get_stub()
        country = stockService_pb2.Country(name=country)
        response = stub.GetProductsFromCountry(country)
        return list(response.products)

    def get_stub(self):
        channel = self.balancer.get_channel()
        stub = stockService_pb2_grpc.StockServiceStub(channel)
        print("Using " + str(channel))
        return stub
