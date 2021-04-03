# open a gRPC channel
import grpc

import geoService_pb2
import geoService_pb2_grpc

channel = grpc.insecure_channel('localhost:50058')

# create a stub (client)
stub = geoService_pb2_grpc.GeoServiceStub(channel)

# create a valid request message
country = geoService_pb2.Empty()

# make the call
response = stub.GetAllCountries(country)

# et voilà
print(response.countries)
