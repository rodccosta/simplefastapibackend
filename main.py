#from <biblioteca> import <função = classe>
#import biblioteca 

import os
import shutil
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

#persistencia local 
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.mount("/static", StaticFiles(directory="static"), name="static")
#tipos = GET = Ler / Post = Criar / Delete = Remover / Put = Atualizar
#@app.<tipo de requisição>

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()
@app.get("/enviar.html", response_class=HTMLResponse)
async def serve_enviar():
    with open("static/enviar.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/api/upload")
async def upload(file: UploadFile = File(...)):
    caminho = os.path.join("uploads", file.filename)
    with open(caminho, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "mensagem": "Arquivo enviado com sucesso"}

@app.get("/api/imagens")
def listar_imagens():
    arquivos = os.listdir("uploads")
    imagens = [f for f in arquivos if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp"))]
    return imagens

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
