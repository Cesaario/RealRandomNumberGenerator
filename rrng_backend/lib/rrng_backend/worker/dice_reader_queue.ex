defmodule RrngBackend.DiceReaderQueue do

  @lock_name :dice_reader_lock
  @lock_limit 1

  def initialize_lock do
    ExSleeplock.new(@lock_name, @lock_limit)
  end

  def obter_face_dado() do
    ExSleeplock.acquire(@lock_name)

    result =
      try do
        :timer.tc(RrngBackend.GrpcClient, :obter_numero, [])
      after
        ExSleeplock.release(@lock_name)
      end

    result
  end

  def get_queue_info() do
    ExSleeplock.lock_state(@lock_name)
  end
end
