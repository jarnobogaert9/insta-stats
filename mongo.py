import pymongo
from dotenv import load_dotenv
import os
load_dotenv()

class MongoClient():
    def __init__(self):
        super().__init__()
        self.client = pymongo.MongoClient(os.getenv('DATABASE_URL'))

    def db(self, name='instadb'):
        return self.client[name]
    
    def insert_one(self, data, coll):
        db = self.db()
        c = db[coll]
        c.insert_one(data)

    def find(self, query, coll):
        db = self.db()
        c = db[coll]
        cursor = c.find(query)
        elements = [{item: x[item] for item in x if item != '_id'} for x in cursor]
        elements.reverse()
        return elements