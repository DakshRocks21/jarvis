import requests
from jarvis.core.console import ConsoleManager

def internet_connectivity_check(url='http://www.google.com/', timeout=2):
    """
    Checks for internet connection availability based on google page.
    """
    console = ConsoleManager()
    try:
        _ = requests.get(url, timeout=timeout)
        console.console_output(info_log='Internet connection passed!')
        return True
    except requests.ConnectionError:
        console.console_output(warn_log="No internet connection.")
        console.console_output(warn_log="Fuctions with internet connection will not work")
        return False