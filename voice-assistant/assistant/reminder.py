import time
from assistant.speech import speak
from threading import Thread

def set_reminder(seconds, message):
    time.sleep(seconds)
    speak(f"Reminder: {message}")

def start_reminder(seconds, message):
    Thread(target=set_reminder, args=(seconds, message)).start()
