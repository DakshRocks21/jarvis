import pyttsx3

class TTSManager:
    """
    Text to speech engine
    """
    def __init__(self) -> None:
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 170)
        self.engine.setProperty('volume', 1.0)
    
    def say(self, text: str) -> None:
        """
        Say text
        """
        self.engine.say(text)
        self.engine.runAndWait()

    def stop(self):
        """
        Stop the TTS engine
        """
        self.engine.stop()


"""

    def get_voices(self) -> list:
        tts_engine = self.__init__()
        return tts_engine.getProperty('voices')
    
    def get_rate(self) -> int:
        tts_engine = self.__init__()
        return tts_engine.getProperty('rate')
    
    def get_volume(self) -> float:
        tts_engine = self.__init__()
        return tts_engine.getProperty('volume')
    
    def set_rate(self, rate: int) -> None:
        tts_engine = self.__init__()
        tts_engine.setProperty('rate', rate)
    
    def set_volume(self, volume: float) -> None:
        tts_engine = self.__init__()
        tts_engine.setProperty('volume', volume)
    
    def get_voices(self) -> list:
        tts_engine = self.__init__()
        return tts_engine.getProperty('voices')
    
    def get_voice(self) -> str:
        tts_engine = self.__init__()
        return tts_engine.getProperty('voice')
    
    def get_voice_id(self) -> str:
        tts_engine = self.__init__()
        return tts_engine.getProperty('voice').id
    
    def get_voice_name(self) -> str:
        tts_engine = self.__init__()
        return tts_engine.getProperty('voice').name

    def get_voice_language(self) -> str:
        tts_engine = self.__init__()
        return tts_engine.getProperty('voice').languages

    def get_voice_identifier(self) -> str:
        tts_engine = self.__init__()
        return tts_engine.getProperty('voice').identifier

    def get_voice_age(self) -> int:
        tts_engine = self.__init__()
        return tts_engine.getProperty('voice').age
"""
