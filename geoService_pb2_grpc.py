# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import geoService_pb2 as geoService__pb2


class GeoServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllCountries = channel.unary_unary(
                '/GeoService/GetAllCountries',
                request_serializer=geoService__pb2.Empty.SerializeToString,
                response_deserializer=geoService__pb2.GetAllCountriesReply.FromString,
                )
        self.GetSubCountries = channel.unary_unary(
                '/GeoService/GetSubCountries',
                request_serializer=geoService__pb2.Country.SerializeToString,
                response_deserializer=geoService__pb2.GetSubCountriesReply.FromString,
                )
        self.GetCities = channel.unary_unary(
                '/GeoService/GetCities',
                request_serializer=geoService__pb2.SubCountry.SerializeToString,
                response_deserializer=geoService__pb2.GetCitiesReply.FromString,
                )
        self.GetLocationOfIp = channel.unary_unary(
                '/GeoService/GetLocationOfIp',
                request_serializer=geoService__pb2.Ip.SerializeToString,
                response_deserializer=geoService__pb2.GetLocationOfIpReply.FromString,
                )


class GeoServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllCountries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSubCountries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCities(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLocationOfIp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GeoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllCountries': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllCountries,
                    request_deserializer=geoService__pb2.Empty.FromString,
                    response_serializer=geoService__pb2.GetAllCountriesReply.SerializeToString,
            ),
            'GetSubCountries': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSubCountries,
                    request_deserializer=geoService__pb2.Country.FromString,
                    response_serializer=geoService__pb2.GetSubCountriesReply.SerializeToString,
            ),
            'GetCities': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCities,
                    request_deserializer=geoService__pb2.SubCountry.FromString,
                    response_serializer=geoService__pb2.GetCitiesReply.SerializeToString,
            ),
            'GetLocationOfIp': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLocationOfIp,
                    request_deserializer=geoService__pb2.Ip.FromString,
                    response_serializer=geoService__pb2.GetLocationOfIpReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GeoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GeoService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllCountries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GeoService/GetAllCountries',
            geoService__pb2.Empty.SerializeToString,
            geoService__pb2.GetAllCountriesReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSubCountries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GeoService/GetSubCountries',
            geoService__pb2.Country.SerializeToString,
            geoService__pb2.GetSubCountriesReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCities(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GeoService/GetCities',
            geoService__pb2.SubCountry.SerializeToString,
            geoService__pb2.GetCitiesReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLocationOfIp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GeoService/GetLocationOfIp',
            geoService__pb2.Ip.SerializeToString,
            geoService__pb2.GetLocationOfIpReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
