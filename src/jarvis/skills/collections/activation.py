import sys

from jarvis.skills.skill import AssistantSkill

class ActivationSkills(AssistantSkill):
    def __init__(self):
        pass

    @classmethod
    def activate(cls):
        #TODO: Implement this method
        print("Activating...")
        
    @classmethod
    def deactivate(cls):
        # TODO: Implement this method
        cls.response("Bye. Shutting Down Now")
        cls.add_log(info_log='Application terminated.')
        sys.exit(0)
        

