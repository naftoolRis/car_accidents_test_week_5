from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
accident_db = db[COLLECTION_NAME]
