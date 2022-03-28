
from jarvis.core.console import ConsoleManager
from jarvis.skills.collections.history import CommandHistory

class TTTManager:

    def __init__(self) -> None:
        self.console = ConsoleManager()
        self.history = CommandHistory()
        self.console.add_log(info_log="Initializing TTT...")
        self.console.add_log(info_log="TTT is ready to go!")

    def listen(self):
        cmd = str(input(">> "))
        # if cmd in 
        self.history.add_entry(entry=cmd)
        self.console.add_log(info_log=f"You said: {cmd}")

