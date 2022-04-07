#from ..db import db
from db import db
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from bson.json_util import dumps

router = APIRouter()

@router.get("/films", tags=["films"])
def read_films_all():
    res = db.getCollection('sample_mflix', 'movies', 10)
    
    return res