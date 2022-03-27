from jarvis.core.console import ConsoleManager
from jarvis.core.process import ProcessManager
from jarvis.utils.startup import internet_connectivity_check


def main():
    console = ConsoleManager()
    console.console_output(info_log='Doing something...')
    internet_connectivity_check()
    console.console_output(info_log='Checks Passed')
    process = ProcessManager()
    process.start()

if __name__ == '__main__':
    main()