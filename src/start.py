from jarvis.core.console import ConsoleManager
from jarvis.core.process import ProcessManager

def main():
    console = ConsoleManager()
    console.console_output(info_log='Doing something...')
    # Add System Checks here
    console.console_output(info_log='Checks Passed')
    process = ProcessManager()
    process.start()

if __name__ == '__main__':
    main()