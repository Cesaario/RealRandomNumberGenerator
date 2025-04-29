defmodule RrngBackend.DiceReaderQueue do

  @lock_name :dice_reader_lock
  @lock_limit 1
  @timeout 5 * 60 * 1000

  def initialize_lock do
    ExSleeplock.new(@lock_name, @lock_limit)
  end

  def obter_face_dado() do
    ExSleeplock.acquire(@lock_name)

    result =
      try do
        RrngBackend.GrpcClient.obter_numero()
      after
        ExSleeplock.release(@lock_name)
      end

    case result do
      {:ok, numero} -> {:ok, numero}
      error -> error
    end
  end

  def get_queue_info() do
    ExSleeplock.lock_state(@lock_name)
  end
end
