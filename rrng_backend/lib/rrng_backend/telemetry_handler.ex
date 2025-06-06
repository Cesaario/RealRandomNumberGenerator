defmodule RrngBackend.TelemetryStatisticsHandler do
  require Logger
  alias RrngBackend.Repo

  def handle_event([:phoenix, :endpoint, :stop], %{duration: duration_ns}, %{conn: conn}, _config) do
    try do

    request_duration_ms = System.convert_time_unit(duration_ns, :native, :millisecond)
    processing_duration_ms = System.convert_time_unit(conn.assigns.processing_duration, :microsecond, :millisecond)
    wait_time_ms = request_duration_ms - processing_duration_ms

    number = Map.get(conn.assigns, :number, 0)

    # Example: log it
    Logger.info("Path: #{conn.request_path}")
    Logger.info("Total duration: #{request_duration_ms} ms")
    Logger.info("Processing duration: #{processing_duration_ms} ms")
    Logger.info("Status: #{conn.status}")
    Logger.info("Number: #{number}")

    Repo.insert_request(conn.status == 200, number, wait_time_ms, request_duration_ms)
    rescue
      e ->
        Logger.error("Error while handling telemetry event: #{inspect(e)}")
    end
  end
end
