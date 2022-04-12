import asyncio
import json
from operator import contains
from prisma import Prisma
from fastapi.encoders import jsonable_encoder
from prisma.models import netflix_titles

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
async def search(column, query):
    await db.connect()
    res = await db.netflix_titles.find_many(
        take=10,
        where={
            column :{
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

async def filter_rating(rating):
    await db.connect()
    res = await db.netflix_titles.find_many(
        where={
            'rating' :{
                'equals': rating,
            }
        }
    )
    res_json = jsonable_encoder(res)
    await db.disconnect()
    return res_json