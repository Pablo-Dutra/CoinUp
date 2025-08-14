from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.database import Base

class TipoConta(Base):
    __tablename__ = "tipoconta"
    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    ativo = Column(Boolean, default=True)
    contas = relationship("Conta", back_populates="tipo")

class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    ativo = Column(Boolean, default=True)
    valorInicial = Column(Float, nullable=False)
    dataCriacao = Column(DateTime(timezone=True), server_default=func.now())
    idTipo = Column(Integer, ForeignKey("tipoconta.id"), nullable=False)
    tipo = relationship("TipoConta", back_populates="contas")
