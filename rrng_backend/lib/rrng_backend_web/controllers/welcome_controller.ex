defmodule RrngBackendWeb.WelcomeController do
  use RrngBackendWeb, :controller

  def index(conn, _params) do
    conn
    |> put_status(:ok)
    |> json(%{message: "Hello :^)", status: :ok})
  end
end
