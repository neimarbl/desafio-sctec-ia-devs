from pydantic import BaseModel, EmailStr
from enum import Enum

# Lista definida para o Segmento conforme o edital
class SegmentoEnum(str, Enum):
    tecnologia = "Tecnologia"
    comercio = "Comércio"
    industria = "Indústria"
    servicos = "Serviços"
    agronegocio = "Agronegócio"

# Lista de principais municípios de SC (pode ser expandida)
class MunicipioSC(str, Enum):
    florianopolis = "Florianópolis"
    balneario_camboriu = "Balneário Camboriú"
    blumenau = "Blumenau"
    chapeco = "Chapecó"
    criciuma = "Criciúma"
    itajai = "Itajaí"
    jaragua_do_sul = "Jaraguá do Sul"
    joinville = "Joinville"
    lages = "Lages"
    sao_jose = "São José"

class EmpreendimentoBase(BaseModel):
    nome: str
    responsavel: str
    municipio: MunicipioSC # Dropdown no Swagger
    segmento: SegmentoEnum  # Dropdown no Swagger
    contato: EmailStr       # Valida @ e domínio (exige pip install pydantic[email])
    status: bool = True

class EmpreendimentoCreate(EmpreendimentoBase):
    pass

class Empreendimento(EmpreendimentoBase):
    id: int

    class Config:
        from_attributes = True
