from assistant.speech import speak, listen
from assistant.processor import process_command

def main():
    speak("Hello! I am your personal assistant.")
    while True:
        command = listen()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()
