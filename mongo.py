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
        
        elements = [{prop: str(row[prop]) if prop == '_id' else row[prop] for prop in row} for row in cursor]
        
        elements.reverse()
        return elements