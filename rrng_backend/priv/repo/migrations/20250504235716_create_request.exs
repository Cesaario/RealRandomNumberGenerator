defmodule RrngBackend.Repo.Migrations.CreateRequest do
  use Ecto.Migration

  def change do
    create table(:request) do
      add :number, :integer
      add :wait_time, :integer
      add :total_time, :integer
      add :success, :boolean, default: false, null: false

      timestamps(type: :utc_datetime)
    end
  end
end
