import requests
from playsound import playsound
import os
def internet_connectivity_check(url='http://www.google.com/', timeout=2):
    """
    Checks for internet connection availability based on google page.
    """
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False
        
def play_activation_sound():
    """
    Plays a sound when the assistant enables.
    """
    # utils_dir = os.path.dirname(__file__)
    # activation_soundfile = os.path.join(utils_dir, '..', 'files', 'activation_sound.wav')
    # playsound(activation_soundfile, block=False)