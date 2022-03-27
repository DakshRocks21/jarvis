from jarvis.core.console import ConsoleManager
from jarvis.engine.stt import STTManager
from jarvis.engine.tts import TTSManager

class ProcessManager:
    def __init__(self):
        self.console = ConsoleManager()
        self.console.console_output(info_log="Initializing Processes...")
        self.stt = STTManager()
        self.tts = TTSManager()

    def start(self):
        self.console.console_output(info_log="Starting Processes...")
        self.console.console_output(info_log="Jarvis is ready to go!")
    
    def stop(self):
        self.console.console_output(info_log="Stopping Processes...")
        self.tts.stop()
        self.stt.stop()
        self.console.console_output(info_log="Jarvis is stopped!")
    
    # def restart(self):
    #     self.console.console_output(info_log="Restarting Processes...")
    #     self.console.console_output(info_log="Jarvis has restarted!") 

    
    def status(self):
        self.console.console_output(info_log="Jarvis is running!")
    