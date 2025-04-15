defmodule RrngBackendWeb.NumeroController do
  use RrngBackendWeb, :controller

  def index(conn, _params) do
    resultado_numero = RrngBackend.GrpcClient.obter_numero()

    case resultado_numero
    do
      {:ok, numero} ->
        conn
        |> put_status(:ok)
        |> json(%{numero: numero})
      {:error, reason} ->
        conn
        |> put_status(:internal_server_error)
        |> json(%{error: "Erro ao obter número: #{reason}"})
    end

    conn
    |> put_status(:ok)
    |> json(%{numero: RrngBackend.GrpcClient.obter_numero()})
  end
end
