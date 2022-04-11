import asyncio
from prisma import Client
from prisma.models import netflix_titles
#from prisma import Prisma
import prisma

async def init(): #used for testing
    db = Client()
    #db = netflix_titles.prisma()._client
    await db.connect()
    
    """
    res = await db.netflix_titles.find_first(
        where={
            'type': {
                'contains': 'Movie'
            }
        }
    )
    """
   
    #res_json = res
    #print(res_json)

    #await db.disconnect()
    
    

def get_all():
    
    return "Temporary Return"


