from jarvis.utils.startup import internet_connectivity_check
from jarvis.utils.console import *

def status():
    if internet_connectivity_check():
        x = print_Green(message="All Systems is running!")
        return x
    else:
        x = print_Red(message="Internet is not connected!")
        return x