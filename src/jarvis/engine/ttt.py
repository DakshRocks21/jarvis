
from jarvis.core.console import ConsoleManager

class TTTManager:
    def __init__(self) -> None:
        self.console = ConsoleManager()
        self.console.console_output(info_log="Initializing TTT...")
        self.console.console_output(info_log="TTT is ready to go!")

    def listen(self):
        cmd = str(input(">> "))
