from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME1, COLLECTION_NAME2

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
accident_db = db[COLLECTION_NAME1]
injuries_db = db[COLLECTION_NAME2]