defmodule RrngBackend.GrpcClient do
  def obter_numero do
    with {:ok, channel} <- GRPC.Stub.connect("localhost:50051"),
         {:ok, response} <- Numero.Stub.obter_numero(channel, %RequisicaoNumero{}) do
      {:ok, response.numero}
    else
      {:error, reason} -> {:error, reason}
    end
  end
end
