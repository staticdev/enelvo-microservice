# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import normalization_pb2 as normalization__pb2


class NormalizationStub(object):
    """Interface for normalization."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetNormalization = channel.unary_unary(
            "/normalization.Normalization/GetNormalization",
            request_serializer=normalization__pb2.Message.SerializeToString,
            response_deserializer=normalization__pb2.Message.FromString,
        )


class NormalizationServicer(object):
    """Interface for normalization."""

    def GetNormalization(self, request, context):
        """Gets normalization from one message."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_NormalizationServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetNormalization": grpc.unary_unary_rpc_method_handler(
            servicer.GetNormalization,
            request_deserializer=normalization__pb2.Message.FromString,
            response_serializer=normalization__pb2.Message.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "normalization.Normalization", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Normalization(object):
    """Interface for normalization."""

    @staticmethod
    def GetNormalization(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/normalization.Normalization/GetNormalization",
            normalization__pb2.Message.SerializeToString,
            normalization__pb2.Message.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
