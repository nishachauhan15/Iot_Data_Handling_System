# mongodb_integration/database.py
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['iot_data']
collection = db['messages']

def insert_into_mongodb(message):
    result = collection.insert_one(message)
    print("Message inserted with ID:", result.inserted_id)
