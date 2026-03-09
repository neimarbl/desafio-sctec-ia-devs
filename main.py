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
