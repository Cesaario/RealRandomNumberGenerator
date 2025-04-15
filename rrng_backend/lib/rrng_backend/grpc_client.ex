defmodule RrngBackend.GrpcClient do
  def obter_numero do
    {:ok, channel} = GRPC.Stub.connect("localhost:50051")
    request = %RequisicaoNumero{}

    case Numero.Stub.obter_numero(channel, request) do
      {:ok, response} -> {:ok, response.numero}
      {:error, reason} -> {:error, reason}
    end
  end
end
