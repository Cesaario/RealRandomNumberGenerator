defmodule RrngBackendWeb.InfoController do
  use RrngBackendWeb, :controller

  def queue(conn, _params) do
    queue_state = RrngBackend.DiceReaderQueue.get_queue_info()

    conn
    |> put_status(:ok)
    |> json(queue_state)
  end
end
