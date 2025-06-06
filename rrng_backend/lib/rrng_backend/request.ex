defmodule RrngBackend.Request do
  use Ecto.Schema
  import Ecto.Changeset

  schema "request" do
    field :success, :boolean, default: false
    field :number, :integer
    field :wait_time, :integer
    field :total_time, :integer

    timestamps(type: :utc_datetime)
  end

  @doc false
  def changeset(request, attrs) do
    request
    |> cast(attrs, [:number, :wait_time, :total_time, :success])
    |> validate_required([:number, :wait_time, :total_time, :success])
  end
end
