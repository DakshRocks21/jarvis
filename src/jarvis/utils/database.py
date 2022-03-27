from distutils.command.config import config
import pymongo

from jarvis.settings import DATABASE_CONFIG

class MongoDB:
    def __init__(self):
        self.config = DATABASE_CONFIG
        self.client = pymongo.MongoClient(f"mongodb://{self.config['host']}:{self.config['port']}/")
        self.db = self.client[f"{self.config['database']}"]
        self.collection = self.db["logs"]
    
    def add_log(self, log):
        self.collection.insert_one(log)
    
    def get_logs(self):
        for x in self.collection.find():
            print(x)
        return self.collection.find()
    
    def get_logs_by_time(self, time):
        return self.collection.find({"date": time})
    
    def get_logs_by_level(self, level):
        return self.collection.find({"level": level})
    
    

"""
x = MongoDB()
x.add_logs([
    {"date": "12-12-12", "message": "This is a sample log message", "level": "info"}, 
    {"date": "12-12-12", "message": "This is a sample log message", "level": "info"}])
x.get_logs()
"""