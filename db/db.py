import json
import os
from dotenv import load_dotenv
from distutils.log import error
import pymongo
from bson.json_util import dumps, loads
from pymongo import *

import asyncio
import motor.motor_asyncio

load_dotenv() #usage for environment variables

conn_str=os.environ["MONGODB_URL"]

client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
#client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)
loop = asyncio.get_event_loop()

def init_client(): #used for testing connection to MongoDB Cluster
    
    db = client["sample_mflix"]
    #movie_collection = db['movies']
    
    try:
        print(db.list_collection_names())
    except Exception:
        print("Unable to Connect")
    
    return client

def getCollection(database, collection, limit):
    
    db = client[database]

    chosen_collection = db[collection]

    try:
        cursor = chosen_collection.find().limit(limit)
        
    except error:
        cursor = "An Error has Occurred."
    
    


    #The below code is from the PyMongo driver implementation
    list_cur = list(cursor) # turns mongo db cursor into a list
    json_data = json.dumps(list_cur) # turns list into json string
    res_json = json_data # turns the json string into actual JSON
    #res_json = jsonable_encoder(list_cur) # actually turns that string into JSON

    return res_json


