defmodule RrngBackend.DiceReaderQueue do
  use GenServer

  @lock_name :dice_reader_lock
  @lock_limit 1
  @timeout 5 * 60 * 1000

  def start_link(_opts) do
    IO.puts("Starting DiceReaderQueue GenServer")
    GenServer.start_link(__MODULE__, :ok, name: __MODULE__)
  end

  @impl true
  def init(:ok) do
    IO.puts("Initializing DiceReaderQueue GenServer")
    ExSleeplock.new(@lock_name, @lock_limit)

    {:ok, %{}}
  end

  def obter_face_dado() do
    GenServer.call(__MODULE__, :get_lock_state, @timeout)
  end

  @impl true
  def handle_call(:get_lock_state, _from, state) do
    ExSleeplock.acquire(@lock_name)
    {:ok, numero} = RrngBackend.GrpcClient.obter_numero()
    ExSleeplock.release(@lock_name)

    {:reply, {:ok, numero}, state}
  end

end
