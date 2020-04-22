from pymongo import MongoClient
import os
client = MongoClient(
    os.getenv("MONGO_HOST"), 
    int(os.getenv("MONGO_PORT")),
    username=os.getenv("MONGO_USERNAME"),
    password=os.getenv("MONGO_PASSWORD"))

db = client.surveys