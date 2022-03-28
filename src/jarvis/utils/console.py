
def print_Red(message): return "\033[91m{}\033[00m" .format(message)
def print_Green(message): return "\033[92m{}\033[00m" .format(message)
def print_Yellow(message): return "\033[93m{}\033[00m" .format(message)
def print_LightPurple(
    message): return "\033[94m{}\033[00m" .format(message)

def print_Purple(message): return "\033[95m{}\033[00m" .format(message)
def print_Cyan(message): return "\033[96m{}\033[00m" .format(message)
def print_LightGray(message): return "\033[97m{}\033[00m" .format(message)
def print_Black(message): return "\033[98m{}\033[00m" .format(message)

def logo():
    logo = """
         ██╗ █████╗ ██████╗ ██╗   ██╗██╗███████╗
         ██║██╔══██╗██╔══██╗██║   ██║██║██╔════╝
         ██║███████║██████╔╝██║   ██║██║███████╗
    ██   ██║██╔══██║██╔══██╗╚██╗ ██╔╝██║╚════██║
    ╚█████╔╝██║  ██║██║  ██║ ╚████╔╝ ██║███████║
     ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝                            
    """
    logo = print_Cyan(logo)
    return logo