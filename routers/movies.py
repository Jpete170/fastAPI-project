from db import db
from fastapi import APIRouter, status


router = APIRouter()

@router.get("/films", tags=["films"])
def read_films_all():
    res = "Database Migration Active; No Results Available"
    
    return res