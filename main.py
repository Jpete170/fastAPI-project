from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv


from routers import movies
from db import db

load_dotenv() #for potential .env usage

app = FastAPI()

#Commented out since it's not being used currently
#app.mount("/static", StaticFiles(directory="static"), name="static")

origins =[
    'http://localhost:8000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(movies.router)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    #await db.init()
    
    return templates.TemplateResponse("index.html", {"request": request})