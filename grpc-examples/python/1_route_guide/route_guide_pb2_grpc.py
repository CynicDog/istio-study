# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import route_guide_pb2 as route__guide__pb2

GRPC_GENERATED_VERSION = '1.74.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in route_guide_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class RouteGuideStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetFeature = channel.unary_unary(
                '/routeguide.RouteGuide/GetFeature',
                request_serializer=route__guide__pb2.Point.SerializeToString,
                response_deserializer=route__guide__pb2.Feature.FromString,
                _registered_method=True)
        self.ListFeatures = channel.unary_stream(
                '/routeguide.RouteGuide/ListFeatures',
                request_serializer=route__guide__pb2.Rectangle.SerializeToString,
                response_deserializer=route__guide__pb2.Feature.FromString,
                _registered_method=True)
        self.RecordRoute = channel.stream_unary(
                '/routeguide.RouteGuide/RecordRoute',
                request_serializer=route__guide__pb2.Point.SerializeToString,
                response_deserializer=route__guide__pb2.RouteSummary.FromString,
                _registered_method=True)
        self.RouteChat = channel.stream_stream(
                '/routeguide.RouteGuide/RouteChat',
                request_serializer=route__guide__pb2.RouteNote.SerializeToString,
                response_deserializer=route__guide__pb2.RouteNote.FromString,
                _registered_method=True)


class RouteGuideServicer(object):
    """Interface exported by the server.
    """

    def GetFeature(self, request, context):
        """A simple RPC.

        Obtains the feature at a given position.

        A feature with an empty name is returned if there's no feature at the given
        position.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFeatures(self, request, context):
        """A server-to-client streaming RPC.

        Obtains the Features available within the given Rectangle.  Results are
        streamed rather than returned at once (e.g. in a response message with a
        repeated field), as the rectangle may cover a large area and contain a
        huge number of features.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RecordRoute(self, request_iterator, context):
        """A client-to-server streaming RPC.

        Accepts a stream of Points on a route being traversed, returning a
        RouteSummary when traversal is completed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RouteChat(self, request_iterator, context):
        """A Bidirectional streaming RPC.

        Accepts a stream of RouteNotes sent while a route is being traversed,
        while receiving other RouteNotes (e.g. from other users).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RouteGuideServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetFeature': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFeature,
                    request_deserializer=route__guide__pb2.Point.FromString,
                    response_serializer=route__guide__pb2.Feature.SerializeToString,
            ),
            'ListFeatures': grpc.unary_stream_rpc_method_handler(
                    servicer.ListFeatures,
                    request_deserializer=route__guide__pb2.Rectangle.FromString,
                    response_serializer=route__guide__pb2.Feature.SerializeToString,
            ),
            'RecordRoute': grpc.stream_unary_rpc_method_handler(
                    servicer.RecordRoute,
                    request_deserializer=route__guide__pb2.Point.FromString,
                    response_serializer=route__guide__pb2.RouteSummary.SerializeToString,
            ),
            'RouteChat': grpc.stream_stream_rpc_method_handler(
                    servicer.RouteChat,
                    request_deserializer=route__guide__pb2.RouteNote.FromString,
                    response_serializer=route__guide__pb2.RouteNote.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'routeguide.RouteGuide', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('routeguide.RouteGuide', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RouteGuide(object):
    """Interface exported by the server.
    """

    @staticmethod
    def GetFeature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/routeguide.RouteGuide/GetFeature',
            route__guide__pb2.Point.SerializeToString,
            route__guide__pb2.Feature.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListFeatures(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/routeguide.RouteGuide/ListFeatures',
            route__guide__pb2.Rectangle.SerializeToString,
            route__guide__pb2.Feature.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RecordRoute(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(
            request_iterator,
            target,
            '/routeguide.RouteGuide/RecordRoute',
            route__guide__pb2.Point.SerializeToString,
            route__guide__pb2.RouteSummary.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RouteChat(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/routeguide.RouteGuide/RouteChat',
            route__guide__pb2.RouteNote.SerializeToString,
            route__guide__pb2.RouteNote.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
