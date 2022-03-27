import json
class Settings:
    def __init__(self):
        self.settings_file = "src/jarvis/settings.json"
        self.settings = self.readJson()
    
    def readJson(self):
        with open(self.settings_file, "r") as f:
            return json.load(f)
config = Settings().readJson()

DATABASE_CONFIG = config["database"]
