from jarvis.core.console import ConsoleManager
from jarvis.engine.stt import STTManager
from jarvis.engine.tts import TTSManager
from jarvis.engine.ttt import TTTManager
from jarvis.utils.startup import internet_connectivity_check, play_activation_sound
class ProcessManager:
    def __init__(self):
        self.console = ConsoleManager()
        self.console.add_log(info_log="Initializing Processes...")
        self.stt = STTManager()
        self.tts = TTSManager()
        self.ttt = TTTManager()

    def start(self):
        self.console.add_log(info_log="Starting Processes...")
        self.console.add_log(info_log="Jarvis is ready to go!")
        play_activation_sound()
        while True:
            self.console.print_dashboard()
            self.ttt.listen()
    
    def stop(self):
        self.console.add_log(info_log="Stopping Processes...")
        self.tts.stop()
        self.stt.stop()
        self.console.add_log(info_log="Jarvis is stopped!")
    
    # def restart(self):
    #     self.console.add_log(info_log="Restarting Processes...")
    #     self.console.add_log(info_log="Jarvis has restarted!") 

