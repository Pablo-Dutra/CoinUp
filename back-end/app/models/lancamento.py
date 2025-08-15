
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.database import Base

class Lancamento(Base):
    __tablename__ = "lancamentos"
    id = Column(Integer, primary_key=True, index=True)
    idReferencia = Column(Integer, nullable=False)
    idCategoria = Column(Integer, ForeignKey("categoria.id"), nullable=False)
    idConta = Column(Integer, ForeignKey("conta.id"), nullable=False)
    idTipoTransacao = Column(Integer, ForeignKey("tipotransacao.id"), nullable=False)
    dataLancamento = Column(DateTime(timezone=True), server_default=func.now())
    dataTransacao = Column(DateTime(timezone=True), nullable=False)
    descricao = Column(String, nullable=False)
    valor = Column(Float, nullable=False)

    categoria = relationship("Categoria")
    conta = relationship("Conta")
    tipotransacao = relationship("TipoTransacao")

class TipoTransacao(Base):
    __tablename__ = "tipotransacao"
    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)