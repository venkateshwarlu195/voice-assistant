from assistant.speech import speak, listen
from assistant.weather import get_weather
from assistant.news import get_news
from assistant.reminder import start_reminder

def process_command(command):
    if "weather" in command:
        speak("Which city?")
        city = listen()
        get_weather(city)

    elif "news" in command:
        get_news()

    elif "reminder" in command:
        speak("What should I remind you about?")
        message = listen()
        speak("In how many seconds?")
        seconds = int(listen())
        start_reminder(seconds, message)

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that")
