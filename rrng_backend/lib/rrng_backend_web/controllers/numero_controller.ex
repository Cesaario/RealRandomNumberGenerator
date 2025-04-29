defmodule RrngBackendWeb.NumeroController do
  use RrngBackendWeb, :controller

  def index(conn, _params) do
    resultado_numero = RrngBackend.DiceReaderQueue.obter_face_dado()

    IO.puts("Resultado do número: #{inspect(resultado_numero)}")

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
  end
end
