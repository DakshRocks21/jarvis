from jarvis.core.console import ConsoleManager
from jarvis.engine.stt import STTManager
from jarvis.engine.tts import TTSManager
from jarvis.engine.ttt import TTTManager
from jarvis.utils.startup import internet_connectivity_check

class ProcessManager:
    def __init__(self):
        self.console = ConsoleManager()
        self.console.console_output(info_log="Initializing Processes...")
        self.stt = STTManager()
        self.tts = TTSManager()
        self.ttt = TTTManager()

    def start(self):
        self.console.console_output(info_log="Starting Processes...")
        self.console.console_output(info_log="Jarvis is ready to go!")
        while True:
            self.console.dashboard()
            self.ttt.listen()
    
    def stop(self):
        self.console.console_output(info_log="Stopping Processes...")
        self.tts.stop()
        self.stt.stop()
        self.console.console_output(info_log="Jarvis is stopped!")
    
    # def restart(self):
    #     self.console.console_output(info_log="Restarting Processes...")
    #     self.console.console_output(info_log="Jarvis has restarted!") 

