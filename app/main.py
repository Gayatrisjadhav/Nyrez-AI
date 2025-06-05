from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.rag_chain import qa_chain

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/ask")
async def ask(question: str):
    try:
        result = qa_chain.invoke({"query": question})
        return {"answer": result['result']}
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}
