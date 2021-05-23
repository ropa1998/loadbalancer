# open a gRPC channel
import grpc

import stockService_pb2_grpc
import stockService_pb2


channel = grpc.insecure_channel('localhost:40041')

# create a stub (client)
stub = stockService_pb2_grpc.StockServiceStub(channel)

# create a valid request message
country = stockService_pb2.CountryProduct(name="Uruguay")

# make the call
response = stub.GetProductsFromCountry(country)

# et voilà
print(response)