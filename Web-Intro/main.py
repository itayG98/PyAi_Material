from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse, FileResponse

app: FastAPI = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    return RedirectResponse(url="/Home")
    # return {"Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"data" :f" Hello {name}"}


@app.get("/click")
async def say_hello():
    return {"data": "Hello user"}


@app.get("/Home")
async def serve_home():
    return FileResponse('static/index.html')

@app.get("/Me")
async def serve_home():
    return FileResponse('static/me.JPG')
