from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Empreendimento(Base):
    __tablename__ = "empreendimentos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    responsavel = Column(String)
    municipio = Column(String)
    segmento = Column(String) # Tecnologia, Comércio, Indústria, Serviços, Agronegócio
    contato = Column(String)
    status = Column(Boolean, default=True) # True = Ativo, False = Inativo
