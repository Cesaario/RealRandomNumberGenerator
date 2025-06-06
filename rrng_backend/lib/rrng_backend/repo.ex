defmodule RrngBackend.Repo do
  alias RrngBackend.Request

  use Ecto.Repo,
    otp_app: :rrng_backend,
    adapter: Ecto.Adapters.Postgres

  def insert_request(success, number, wait_time, total_time) do
    insert(%Request{
      success: success,
      number: number,
      wait_time: wait_time,
      total_time: total_time
    })
  end
end
