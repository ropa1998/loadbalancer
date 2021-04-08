# open a gRPC channel
import grpc

from users_pb2 import LoginRequest
from users_pb2_grpc import UsersStub

channel = grpc.insecure_channel('localhost:9090')

# create a stub (client)
stub = UsersStub(channel)

# create a valid request message
login_request = LoginRequest(email="test@mail.comm", password="12345678")

# make the call
response = stub.Authenticate(login_request)

# et voilà
print(response)
