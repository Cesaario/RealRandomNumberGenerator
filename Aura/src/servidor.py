from concurrent import futures
import grpc
import numero_pb2_grpc
import numero_pb2
import rrng_serial
import rrng_cv

class NumeroServicer(numero_pb2_grpc.NumeroServicer):
    def ObterNumero(self, request, context):
        rrng_serial.iniciar_serial()
        rrng_serial.rodar_dado()
        rrng_serial.encerrar_serial()

        rrng_cv.iniciar_captura()
        face = rrng_cv.obter_face_ate_sucesso()
        rrng_cv.encerrar_captura()

        return numero_pb2.RepostaNumero(numero=face)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    numero_pb2_grpc.add_NumeroServicer_to_server(NumeroServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Servidor gRPC executando...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()