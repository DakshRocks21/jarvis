from matplotlib.pyplot import cla
from jarvis.core.console import ConsoleManager


class AssistantSkill:
    def __init__(self) -> None:
        self.console_maneger = ConsoleManager()
    
    @classmethod
    def add_log(cls, debug_log=None, info_log=None, warning_log=None, error_log=None, critical_log=None) -> str:
        cls.console_maneger.add_log(debug_log=debug_log, info_log=info_log, warning_log=warning_log, error_log=None, critical_log=critical_log)

    @classmethod
    def response(cls, text=None) -> None:
        # TODO: Implement this method
        # cls.console_maneger.response(text=text)
        pass

        

    
    