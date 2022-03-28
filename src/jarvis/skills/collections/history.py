from re import I
from jarvis.skills.skill import AssistantSkill
from jarvis.utils.database import MongoDB


class CommandHistory(AssistantSkill):
    def __init__(self):
        self.db = MongoDB()

    def add_entry(self, entry, collection="history"):
        self.db.add_entry(collection, entry)
    
    def last_5_entries(self, collection="history"):
        return self.db.last_5_entries(collection)