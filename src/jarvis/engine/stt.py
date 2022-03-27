import speech_recognition as sr

from jarvis.core.console import ConsoleManager

class STTManager:
    """
    Speech to Text
    """
    def __init__(self) -> None:
        self.console = ConsoleManager()
        self.console.console_output(debug_log="Initializing STT...")
        self.r = sr.Recognizer()
        self.console.console_output(debug_log="STT initialized.")
        self.r.pause_threshold = 0.5
        self.mic = sr.Microphone()

    def listen(self) -> str:
        """
        Listen to the microphone and return the text
        """
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source)
        try:
            return self.r.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I didn't get that."
        except sr.RequestError as e:
            return "Sorry, my speech service isn't available right now."
    
    def stop(self) -> None:
        """
        Stop the STT engine
        """
        self.console.console_output(debug_log="Stopping STT...")
        self.r.stop_listening()
        self.console.console_output(debug_log="STT stopped.")
