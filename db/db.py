import asyncio
import json
from prisma import Prisma
from fastapi.encoders import jsonable_encoder

db = Prisma()

async def init(): #used for testing
    
    db.connect()
    res = db.netflix_titles.find_first(
        where={
            'title':
            {'contains':'Johnson'}
        }
    )
    res_json = jsonable_encoder(res)
    print(res_json)

    db.disconnect()
    
    

async def get_all():
    
    await db.connect()
    res = await db.netflix_titles.find_many()
    res_json = jsonable_encoder(res)
    #print(res_json)

    await db.disconnect()
    return res_json

async def get_one():
    await db.connect()
    res = await db.netflix_titles.find_first()
    res_json = jsonable_encoder(res)
    await db.disconnect()
    return res_json
    
