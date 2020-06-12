# -*- coding: utf-8 -*-
"""Microservice for enelvo normalization method."""
import logging
from concurrent import futures
from typing import Optional

import enelvo.normaliser
import grpc

import normalization_pb2
import normalization_pb2_grpc


def get_normalization(
    normaliser: enelvo.normaliser.Normaliser, message: str
) -> Optional[str]:
    """Normalizes the message.

    Arguments:
        normaliser: instance of Enelvo.
        message: original message.

    Returns:
        Optional[str]: normalized string.
    """
    try:
        return normaliser.normalise(message)
    except AttributeError:
        return None


class NormalizationServicer(normalization_pb2_grpc.NormalizationServicer):
    """Provides methods that implement functionality of normalization server."""

    def __init__(self):
        """Initializes NormalizationServicer."""
        self.normaliser = enelvo.normaliser.Normaliser(tokenizer="readable")

    def GetNormalization(self, request):
        """Get text normalization.

        Args:
            request: original message.

        Returns:
            str: normalized message.
        """
        reply = get_normalization(self.normaliser, request.text)
        if reply is None:
            return normalization_pb2.Message(text="")
        else:
            return normalization_pb2.Message(text=reply)


def serve():
    """Starts the server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    normalization_pb2_grpc.add_NormalizationServicer_to_server(
        NormalizationServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
