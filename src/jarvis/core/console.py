import os
from datetime import datetime
from jarvis.utils.database import MongoDB

class ConsoleManager:
    def __init__(self):
        self.console_output(debug_log="Initializing ConsoleManager...")
        self.logger = MongoDB()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def add_log(self, level, log):
        x = {
            "date": datetime.now().strftime('%d-%b-%y %H:%M:%S'),
            "message": log,
            "level": level
        }
        MongoDB().add_log(x)

    def console_output(self, debug_log=None, info_log=None, warning_log=None, error_log=None, critical_log=None):
        if debug_log:
            self.add_log("debug", debug_log)
        elif info_log:
            self.add_log("info", info_log)
        elif warning_log:
            self.add_log("warning", warning_log)
        elif error_log:
            self.add_log("error", error_log)
        elif critical_log:
            self.add_log("critical", critical_log)
        else:
            self.add_log("debug", "No log message was provided.")
