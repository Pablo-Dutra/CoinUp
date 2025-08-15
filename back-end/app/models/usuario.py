from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.database.database import Base

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)  # SHA256
    ativo = Column(Boolean, default=True)
    datacriacao = Column(DateTime(timezone=True), server_default=func.now())
    datalateracao = Column(DateTime(timezone=True), onupdate=func.now())
