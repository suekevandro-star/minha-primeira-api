from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def raiz():
    return {"mensagem": "Olá, Engenheiro! Sua API está rodando."}

@app.get("/engenharia")
def engenharia():
    return {"status": "Operacional", "tensao": "220V", "frequencia": "60Hz"}