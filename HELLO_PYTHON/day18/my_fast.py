from fastapi import FastAPI
from fastapi.params import Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jupyter_server.tests.extension.test_launch import fetch
from pydantic import BaseModel
from requests.api import request
import uvicorn
from day18.dao_mem import DaoMem
from starlette.responses import RedirectResponse
from dns.rdataclass import NONE


templates = Jinja2Templates(directory="templates")

class Mem(BaseModel):
    mem_id: str = None
    mem_name: str = None
    tel: str = None
    email: str = None

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    return RedirectResponse("/static/mem.html")

@app.post("/mem_list")
async def mem_list():
    list = DaoMem().selectList()
    return JSONResponse(content={'list' : list})

@app.post("/mem_select")
async def mem_select(mem: Mem):
    vo = DaoMem().select(mem.mem_id)
    return JSONResponse(content={'vo' : vo})

@app.post("/mem_add")
async def mem_add(mem: Mem):
    cnt = DaoMem().insert(mem.mem_id, mem.mem_name, mem.tel, mem.email)
    return JSONResponse(content={'cnt' : cnt})

@app.post("/mem_mod")
async def mem_mod(mem: Mem):
    cnt = DaoMem().update(mem.mem_id, mem.mem_name, mem.tel, mem.email)
    return JSONResponse(content={'cnt' : cnt})

@app.post("/mem_del")
async def mem_del(mem: Mem):
    cnt = DaoMem().delete(mem.mem_id)
    return JSONResponse(content={'cnt' : cnt})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
