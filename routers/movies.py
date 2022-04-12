from db import db
from fastapi import APIRouter, status


router = APIRouter(
    prefix="/api",
    tags=['films']
)

@router.get("/films")
async def get_all_films():
    res = await db.get_all()
    
    return res

#basic search function
@router.get("/films/search")
async def query_db(column: str, query: str):
    res = await db.search(column, query)
    return res

#return document based on id
@router.get('/films/shows/{show_id}')
async def get_show_id(show_id : str):
    res = await db.get_showId(show_id)
    
    return res

#Filter based on types (Movie / TV Show)
@router.get('/films/{type}')
async def filter_type(type: str):
    res = await db.search('type', type)
    return res

#Filter based on ratings
@router.get('/films/ratings/{rating}')
async def filter_rating(rating: str):
    res = await db.filter_rating(rating)
    return res

#Filter based on Country
@router.get('/films/country/{country}')
async def filter_country(country):
    res = await db.search('country', country) #placeholder function
    return res

#Filter based on Release Year
@router.get('/films/year/{year_published}')
async def filter_year(year_published):
    res = await db.search('release_year', year_published) #placeholder function
    return res