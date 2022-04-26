from db import db
from fastapi import APIRouter, status, HTTPException, Response
import os
#response = Response

router = APIRouter(
    prefix="/api",
    tags=['films'],
    
)

origin = os.environ.get("ORIGIN")

@router.get("/films")
async def get_all_films():
    res = await db.get_all()
    
    return res

#basic search function
@router.get("/films/search")
async def query_db(response: Response, column: str, query: str, limit: int | None = None, ):
    response.headers['Access-Control-Allow-Origin'] = origin
    res = await db.search(column, query, limit)
    
    if res is not None:
        return res
    else:
        raise HTTPException(status_code=404, detail="No Results Found.")

#return document based on id
@router.get('/films/shows/{show_id}')
async def get_show_id(show_id, response: Response):
   response.headers['Access-Control-Allow-Origin'] = origin
   
   res = await db.get_showId(show_id)        
   if res is not None:
    return res
   else:
        raise HTTPException(status_code=404, detail="Show Not Found.")

#Filter based on types (Movie / TV Show)
@router.get('/films/{type}')
async def filter_type(response: Response, type: str, limit: int | None = None):
    response.headers['Access-Control-Allow-Origin'] = origin
    res = await db.search('type', type, limit)
    if res is not None:
        return res
    else:
        raise HTTPException(status_code=404, detail="Show Type Not Found.")
    

#Filter based on ratings
@router.get('/films/ratings/{rating}')
async def filter_rating(rating: str, response: Response):
    response.headers['Access-Control-Allow-Origin'] = origin
    res = await db.filter_rating(rating)
    if res is not None:
        return res
    else:
        raise HTTPException(status_code=404, detail="Show Ratings Not Found.")

#Filter based on Country
@router.get('/films/country/{country}')
async def filter_country(response: Response, country: str, limit: int | None = None):
    response.headers['Access-Control-Allow-Origin'] = origin
    res = await db.search('country', country, limit) #placeholder function
    if res is not None:
        return res
    else:
        raise HTTPException(status_code=404, detail="Country Not Found.")

#Filter based on Release Year
@router.get('/films/year/{year_published}')
async def filter_year(response: Response, year_published, limit: int | None = None):
    response.headers['Access-Control-Allow-Origin'] = origin
    res = await db.search('release_year', year_published, limit) #placeholder function
    if res is not None:
        return res
    else:
        raise HTTPException(status_code=404, detail="Release Year Not Found.")