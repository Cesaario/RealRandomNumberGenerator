defmodule RrngBackend.Application do
  # See https://hexdocs.pm/elixir/Application.html
  # for more information on OTP Applications
  @moduledoc false

  use Application

  @impl true
  def start(_type, _args) do
    children = [
      RrngBackendWeb.Telemetry,
      # RrngBackend.Repo,
      {DNSCluster, query: Application.get_env(:rrng_backend, :dns_cluster_query) || :ignore},
      {Phoenix.PubSub, name: RrngBackend.PubSub},
      # Start a worker by calling: RrngBackend.Worker.start_link(arg)
      # {RrngBackend.Worker, arg},
      # Start to serve requests, typically the last entry
      RrngBackendWeb.Endpoint,
      RrngBackend.DiceReaderQueue
    ]

    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: RrngBackend.Supervisor]
    Supervisor.start_link(children, opts)

    DiceReaderQueue.initialize_lock()
  end

  # Tell Phoenix to update the endpoint configuration
  # whenever the application is updated.
  @impl true
  def config_change(changed, _new, removed) do
    RrngBackendWeb.Endpoint.config_change(changed, removed)
    :ok
  end
end
