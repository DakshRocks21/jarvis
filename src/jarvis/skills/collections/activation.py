import sys

from jarvis.skills.skill import AssistantSkill

class ActivationSkills(AssistantSkill):
    def __init__(self):
        pass

    def activate(self):
        pass
    @classmethod
    def deactivate(cls):
        # TODO: Implement this method
        cls.response("Bye. Shutting Down Now")
        cls.console_output(info_log='Application terminated.')
        sys.exit(0)
        

