import grpc
import numero_pb2_grpc
import numero_pb2

channel = grpc.insecure_channel('localhost:50051')
stub = numero_pb2_grpc.NumeroStub(channel)

requisicao = numero_pb2.RequisicaoNumero()
face = stub.ObterNumero(requisicao)
print(face)