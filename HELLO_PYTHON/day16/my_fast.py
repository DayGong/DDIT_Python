from fastapi import FastAPI
import uvicorn
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from day16.dao_mem import DaoMem

templates = Jinja2Templates(directory="templates")
app = FastAPI()

@app.get("/")
@app.get("/mem_list")
async def mem_list(request: Request):
    list = DaoMem().selectList()
    return templates.TemplateResponse("mem_list.html", {'request' : request, 'list' : list})

@app.get("/mem_detail")
async def mem_detail(request: Request, mem_id: str):
    vo = DaoMem().select(mem_id)
    return templates.TemplateResponse("mem_detail.html", {'request' : request, 'vo' : vo})

@app.get("/mem_mod")
async def mem_mod(request: Request, mem_id: str):
    vo = DaoMem().select(mem_id)
    return templates.TemplateResponse("mem_mod.html", {'request' : request, 'vo' : vo})

@app.post("/mem_mod_act")
async def mem_mod_act(request: Request, mem_id: str = Form(), mem_name: str = Form(), tel: str = Form(), email: str = Form()):
    cnt = DaoMem().update(mem_id, mem_name, tel, email)
    return templates.TemplateResponse("mem_mod_act.html", {'request' : request, 'cnt' : cnt})

@app.post("/mem_del_act")
async def mem_del_act(request: Request, mem_id: str = Form()):
    cnt = DaoMem().delete(mem_id)
    return templates.TemplateResponse("mem_del_act.html", {'request' : request, 'cnt' : cnt})

@app.get("/mem_add")
async def mem_add(request: Request):
    return templates.TemplateResponse("mem_add.html", {'request' : request})

@app.post("/mem_add_act")
async def mem_add_act(request: Request, mem_id: str = Form(), mem_name: str = Form(), tel: str = Form(), email: str = Form()):
    cnt = DaoMem().insert(mem_id, mem_name, tel, email)
    return templates.TemplateResponse("mem_add_act.html", {'request' : request, 'cnt' : cnt})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)