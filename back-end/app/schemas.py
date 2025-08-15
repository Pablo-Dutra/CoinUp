from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from pydantic import EmailStr

class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    ativo: Optional[bool] = True

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioOut(UsuarioBase):
    id: int
    datacriacao: datetime
    datalateracao: Optional[datetime]

    class Config:
        from_attributes = True

class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class CategoriaBase(BaseModel):
    descricao: str
    ativo: bool

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaOut(CategoriaBase):
    id: int
    model_config = {
        "from_attributes": True
    }

class TipoContaBase(BaseModel):
    descricao: str
    ativo: bool

class TipoContaCreate(TipoContaBase):
    pass

class TipoContaOut(TipoContaBase):
    id: int
    model_config = {
        "from_attributes": True
    }

class ContaBase(BaseModel):
    nome: str
    ativo: bool
    valorInicial: float
    idTipo: int

class ContaCreate(ContaBase):
    pass

class ContaUpdate(ContaBase):
    pass

class ContaOut(ContaBase):
    id: int
    dataCriacao: datetime
    model_config = {
        "from_attributes": True
    }

class TipoTransacaoBase(BaseModel):
    descricao: str

class TipoTransacaoCreate(TipoTransacaoBase):
    pass

class TipoTransacaoOut(TipoTransacaoBase):
    id: int
    model_config = {
        "from_attributes": True
    }

class LancamentoBase(BaseModel):
    idReferencia: int
    idCategoria: int
    idConta: int
    idTipoTransacao: int
    dataLancamento: datetime = None
    dataTransacao: datetime
    descricao: str
    valor: float

class LancamentoCreate(LancamentoBase):
    pass

class LancamentoOut(LancamentoBase):
    id: int
    dataLancamento: datetime
    model_config = {
        "from_attributes": True
    }

class LancamentoDetalhadoOut(BaseModel):
    id: int
    idReferencia: int
    descricao: str
    idCategoria: int
    categoria_descricao: Optional[str]
    idConta: int
    conta_nome: Optional[str]
    tipoconta_descricao: Optional[str]
    idTipoTransacao: int
    tipotransacao_descricao: Optional[str]
    dataLancamento: datetime
    dataTransacao: datetime
    valor: float
    model_config = {
        "from_attributes": True
    }