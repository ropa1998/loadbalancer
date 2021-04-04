# open a gRPC channel
import yaml
from retrying import retry

from load_balancer.RoundRobinBalancer import RoundRobinBalancer
from users_pb2 import LoginRequest
from users_pb2_grpc import UsersStub

yamlfile = open("/home/matias/projects/facultad/distribuidos/loadbalancer-python/config.yaml", "r")
yaml_info = yaml.load(yamlfile, Loader=yaml.FullLoader)
max_retries = yaml_info["max_retries"]

constants = dict(authenticated="AUTHENTICATED", failed="FAILED")

class AuthServiceClient:

    def __init__(self, channels):
        self.balancer = RoundRobinBalancer(channels)

    @retry(stop_max_attempt_number=max_retries)
    def authenticate(self, email, password):
        stub = self.get_stub()
        login_request = LoginRequest(email=email, password=password)
        try:
            stub.Authenticate(login_request)
            return constants['authenticated']
        except Exception:
            return constants['failed']

    def get_stub(self):
        channel = self.balancer.get_channel()
        stub = UsersStub(channel)
        print("Using " + str(channel))
        return stub
