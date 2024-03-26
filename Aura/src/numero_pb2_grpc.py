# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import numero_pb2 as numero__pb2


class NumeroStub(object):
    """A definição de um serviço contendo um número gerado aleatoriamente
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ObterNumero = channel.unary_unary(
                '/Numero/ObterNumero',
                request_serializer=numero__pb2.RequisicaoNumero.SerializeToString,
                response_deserializer=numero__pb2.RepostaNumero.FromString,
                )


class NumeroServicer(object):
    """A definição de um serviço contendo um número gerado aleatoriamente
    """

    def ObterNumero(self, request, context):
        """Obtém um número aleatório
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NumeroServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ObterNumero': grpc.unary_unary_rpc_method_handler(
                    servicer.ObterNumero,
                    request_deserializer=numero__pb2.RequisicaoNumero.FromString,
                    response_serializer=numero__pb2.RepostaNumero.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Numero', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Numero(object):
    """A definição de um serviço contendo um número gerado aleatoriamente
    """

    @staticmethod
    def ObterNumero(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Numero/ObterNumero',
            numero__pb2.RequisicaoNumero.SerializeToString,
            numero__pb2.RepostaNumero.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
