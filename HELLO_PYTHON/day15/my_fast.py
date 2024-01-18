from fastapi import FastAPI
import uvicorn
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

templates = Jinja2Templates(directory="templates")
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/param")
async def param(menu: str = "짜장면"):
    print("menu",menu)
    return "param:"

@app.post("/post")
async def post(menu: str = Form()):
    print("menu",menu)
    return "post:"+menu

@app.get("/forw")
async def forw(request: Request):
    a = "홍길동"
    b = ["전우치", "역두산", "강호동"]
    c = [
        {'mem_id' : 1, 'mem_name' : 1, 'tel' : 1, 'email' : 1},
        {'mem_id' : 2, 'mem_name' : 2, 'tel' : 2, 'email' : 2}
    ]
    return templates.TemplateResponse("forw.html", {'request': request, 'a' : a, 'b' : b, 'c' : c})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)