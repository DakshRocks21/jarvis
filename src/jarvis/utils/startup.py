import requests

def internet_connectivity_check(url='http://www.google.com/', timeout=2):
    """
    Checks for internet connection availability based on google page.
    """
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False