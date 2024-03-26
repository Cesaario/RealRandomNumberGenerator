from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RequisicaoNumero(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RepostaNumero(_message.Message):
    __slots__ = ("numero",)
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    numero: int
    def __init__(self, numero: _Optional[int] = ...) -> None: ...
