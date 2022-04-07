import os
from dotenv import load_dotenv
from distutils.log import error
import pymongo
from bson.json_util import dumps, loads
from bson.raw_bson import RawBSONDocument
from fastapi.encoders import jsonable_encoder
from yaml import dump

load_dotenv() #usage for environment variables

conn_str=os.environ["MONGODB_URL"]

client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)



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

    chosen_collection = db.get_collection(collection)
    try:
        results = chosen_collection.find().limit(limit)
        
    except error:
        results = "An Error has Occurred."
    
    list_cur = list(results) # turns results into a list
    json_doc = dumps(list_cur)
    res_json = json_doc
    #res_json = jsonable_encoder(list_cur) # actually turns that string into JSON

    return res_json
