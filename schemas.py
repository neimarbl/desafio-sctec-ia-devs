from pydantic import BaseModel, EmailStr
from typing import Optional

# Esquema base (campos comuns)
class EmpreendimentoBase(BaseModel):
    nome: str
    responsavel: str
    municipio: str
    segmento: str # Tecnologia, Comércio, Indústria, Serviços, Agronegócio
    contato: str
    status: bool = True

# Esquema para criação (o que o usuário envia no POST)
class EmpreendimentoCreate(EmpreendimentoBase):
    pass

# Esquema para resposta (o que a API devolve, inclui o ID do banco)
class Empreendimento(EmpreendimentoBase):
    id: int

    class Config:
        from_attributes = True
