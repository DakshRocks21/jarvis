from distutils.command.config import config
import pymongo

from jarvis.settings import DATABASE_CONFIG

class MongoDB:
    def __init__(self):
        self.config = DATABASE_CONFIG
        self.client = pymongo.MongoClient(f"mongodb://{self.config['host']}:{self.config['port']}/")
        self.db = self.client[f"{self.config['database']}"]
        self.collection = self.db[f"{self.config['collection']}"]

    def checkIfCollectionExists(self, collection):
        if collection in self.db.list_collection_names():
            return True
        return False

    def add_entry(self, entry, collection):
        if self.checkIfCollectionExists(collection):
            self.db[collection].insert_one(entry)
    
    def last_5_entries(self, collection):
        y = []
        if self.checkIfCollectionExists(collection):
            for x in self.db[collection].find({}, {"_id":0}).sort("_id",-1).limit(5):
                #print(f"{x['date']} - {x['level']}: {x['message']}")
                y.append(f"{x['date']} - {x['level'].upper()}: {x['message']}")
        return y[::-1]    
