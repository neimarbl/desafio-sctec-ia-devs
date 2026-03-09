from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine

# Cria as tabelas no banco de dados automaticamente ao iniciar
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Empreendedorismo SC - API")

# Função para obter uma conexão com o banco em cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"mensagem": "API de Empreendimentos de Santa Catarina operacional!"}

@app.get("/status")
def status(db: Session = Depends(get_db)):
    return {"status": "online", "banco_conectado": True}

#crud completo
import schemas  # Não esqueça de importar o arquivo de schemas lá no topo!

@app.post("/empreendimentos/", response_model=schemas.Empreendimento, status_code=201)
def criar_empreendimento(obj: schemas.EmpreendimentoCreate, db: Session = Depends(get_db)):
    # Transforma o schema em um modelo do banco
    novo_item = models.Empreendimento(**obj.dict())
    db.add(novo_item)
    db.commit()
    db.refresh(novo_item)
    return novo_item
