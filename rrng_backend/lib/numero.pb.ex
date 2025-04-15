defmodule RequisicaoNumero do
  @moduledoc false

  use Protobuf, protoc_gen_elixir_version: "0.14.1", syntax: :proto3
end

defmodule RepostaNumero do
  @moduledoc false

  use Protobuf, protoc_gen_elixir_version: "0.14.1", syntax: :proto3

  field :numero, 1, type: :int32
end

defmodule Numero.Service do
  @moduledoc false

  use GRPC.Service, name: "Numero", protoc_gen_elixir_version: "0.14.1"

  rpc :ObterNumero, RequisicaoNumero, RepostaNumero
end

defmodule Numero.Stub do
  @moduledoc false

  use GRPC.Stub, service: Numero.Service
end
