from sqlalchemy import Column, Integer, String, Boolean
from database import Base
import schemas 

class Empreendimento(Base):
    __tablename__ = "empreendimentos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    responsavel = Column(String)
    municipio = Column(String)  # O banco armazena o texto do Enum
    segmento = Column(String)  # O banco armazena o texto do Enum
    contato = Column(String)
    status = Column(Boolean, default=True) # True = Ativo, False = Inativo
