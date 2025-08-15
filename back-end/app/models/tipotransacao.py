from sqlalchemy import Column, Integer, String
from app.database.database import Base

class TipoTransacao(Base):
    __tablename__ = "tipotransacao"
    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
