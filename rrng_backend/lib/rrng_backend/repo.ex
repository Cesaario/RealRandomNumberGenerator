defmodule RrngBackend.Repo do
  use Ecto.Repo,
    otp_app: :rrng_backend,
    adapter: Ecto.Adapters.Postgres
end
