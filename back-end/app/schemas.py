
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
