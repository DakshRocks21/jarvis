import os
from datetime import datetime
from jarvis.utils.database import MongoDB
from jarvis.utils.process import status
from jarvis.utils.console import logo
class ConsoleManager:

    def __init__(self):
        self.add_log(debug_log="Initializing ConsoleManager...")
        self.db = MongoDB()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def add_log(self, debug_log=None, info_log=None, warning_log=None, error_log=None, critical_log=None):
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

    def add_log(self, level, log):
        x = {
            "date": datetime.now().strftime('%d-%b-%y %H:%M:%S'),
            "message": log,
            "level": level
        }
        self.db.add_entry(x, "logs")

    def header(self, text=None):
        if text:
            x = f"{(100-len(text.upper()))//2*'-'} {text} {(100-len(text.upper()))//2*'-'}"
        else:
            x = "-"*102
        return x

    def console_output(self, refresh_console=False):
        if refresh_console:
            self.clear()
        print(self.header("Jarvis"))
        print(logo())
        print(self.header("System Information"))
        print(self.header("Status"))
        print(status())
        print(self.header("Logs"))
        for x in self.db.last_5_entries("logs"):
            print(x)
        print(self.header())
