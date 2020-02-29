"""Example implementation of a normalization client."""

from __future__ import print_function
import logging

import grpc

import normalization_pb2
import normalization_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = normalization_pb2_grpc.NormalizationStub(channel)
        response = stub.GetNormalization(normalization_pb2.Message(text='oi td bm?'))
    print("Normalization client received: " + response.text)


if __name__ == '__main__':
    logging.basicConfig()
    run()
