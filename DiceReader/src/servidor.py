from concurrent import futures
import grpc
import numero_pb2_grpc
import numero_pb2
import rrng_serial
import rrng_cv

# Utilizado somente para fins de testes
# Seria um crime usar random no REAL Random Number Generator
import random
import time

MOCK_DADO = True

class NumeroServicer(numero_pb2_grpc.NumeroServicer):
    def ObterNumero(self, request, context):

        if MOCK_DADO:
            time.sleep(2)
            return numero_pb2.RepostaNumero(numero=random.randint(1, 6))

        print("Rodando dado...")
        rrng_serial.rodar_dado()

        print("Lendo face...")
        face = rrng_cv.obter_face_dado_com_captura()
        print("Face obtida", face)

        return numero_pb2.RepostaNumero(numero=face)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    numero_pb2_grpc.add_NumeroServicer_to_server(NumeroServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Servidor gRPC executando na porta 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()