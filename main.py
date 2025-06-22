#from <biblioteca> import <função = classe>
#import biblioteca 


from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from routes import file, person

import uvicorn

app = FastAPI()

app.include_router(file.router)
app.include_router(person.router)

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


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
