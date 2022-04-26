from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from dotenv import load_dotenv
#from dependencies import origins

from routers import movies
from db import db

load_dotenv() #for local .env usage

app = FastAPI()

#Commented out since it's not being used currently
#app.mount("/static", StaticFiles(directory="static"), name="static")

origins =[
    'http://localhost',
    'http://localhost:8000',
    'http://localhost:3000/',
    'http://127.0.0.1:3000/'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(movies.router)

app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=404)

templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    #await db.init()
    
    return templates.TemplateResponse("index.html", {"request": request})

    