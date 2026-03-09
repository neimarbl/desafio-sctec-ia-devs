from fastapi import FastAPI

app = FastAPI(title="Empreendedorismo SC - API")

@app.get("/")
def home():
    return {"mensagem": "API de Empreendimentos de Santa Catarina operacional!"}

@app.get("/status")
def status():
    return {"status": "online", "estado": "Santa Catarina"}
