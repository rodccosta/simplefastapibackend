from fastapi import APIRouter
from fastapi import File, UploadFile
import os
import shutil

router = APIRouter(prefix="/api/images", tags=["Images"])

@router.post("/add")
async def upload(file: UploadFile = File(...)):
    caminho = os.path.join("uploads", file.filename)
    with open(caminho, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "mensagem": "Arquivo enviado com sucesso"}

@router.get("/list")
def listar_imagens():
    arquivos = os.listdir("uploads")
    imagens = [f for f in arquivos if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp"))]
    return imagens
