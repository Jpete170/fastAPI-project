from operator import contains
from fastapi.encoders import jsonable_encoder
from prisma import Prisma


db = Prisma()

# get all records in the database
async def get_all():    
    await db.connect()
    res = await db.netflix_titles.find_many()
    res_json = jsonable_encoder(res)
    

    await db.disconnect()
    return res_json

#search records with multiple parameters
#will be used to handle a majority of page routing
async def search(column, query, limit):
    await db.connect()
    res = await db.netflix_titles.find_many(
        take=limit,
        where={
            column :{
                'contains': query,
            }
        }
    )
    res_json = jsonable_encoder(res)
    await db.disconnect()
    return res_json
    

async def filter_page(Type, column, query, limit):
    await db.connect()
    res = await db.netflix_titles.find_many(
        take=limit,
        where={
            'type': Type,
            column:{
                'contains': query,
            }
        }
    )
    res_json = jsonable_encoder(res)
    await db.disconnect()
    return res_json

#get item show_id
#Will be used to generate individual web pages for each individual entry
async def get_showId(id):
    await db.connect()
    res = await db.netflix_titles.find_first(
        where={
            "show_id": id
        }
    )
    res_json = jsonable_encoder(res)
    await db.disconnect()
    return res_json

#Filter by ratings
async def filter_rating(rating, limit):
    await db.connect()
    res = await db.netflix_titles.find_many(
        take=limit,
        where={
            'rating' :{
                'equals': rating,
            }
        }
    )
    
    res_json = jsonable_encoder(res)
    await db.disconnect()
    return res_json

#Filter by ratings
async def filter_type(type, limit):
    await db.connect()
    res = await db.netflix_titles.find_many(
        take=limit,
        where={
            'type': type,
            
        }
    )
    
    res_json = jsonable_encoder(res)
    await db.disconnect()
    return res_json