defmodule RrngBackendWeb.NumeroController do
  use RrngBackendWeb, :controller
  alias RrngBackend.Repo

  def index(conn, _params) do

    {processing_duration, result} = RrngBackend.DiceReaderQueue.obter_face_dado()


    IO.puts("Resultado do número: #{inspect(result)}")

    case result
    do
      {:ok, number} ->
        conn
        |> assign(:processing_duration, processing_duration)
        |> assign(:number, number)
        |> put_status(:ok)
        |> json(%{numero: number})
      {:error, reason} ->
        conn
        |> assign(:processing_duration, processing_duration)
        |> put_status(:internal_server_error)
        |> json(%{error: "Erro ao obter número: #{reason}"})
    end
  end
end
