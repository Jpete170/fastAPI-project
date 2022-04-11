from db import db
from fastapi import APIRouter, status


router = APIRouter()

@router.get("/films", tags=["films"])
async def read_films_all():
    res = await db.get_all()
    
    return res

@router.get("/film", tags=['films'])
async def read_films_one():
    res = await db.get_one()
    return res