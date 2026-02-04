import requests
from assistant.speech import speak

API_KEY = "YOUR_OPENWEATHER_API_KEY"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    if response.get("main"):
        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]
        speak(f"The temperature in {city} is {temp} degrees with {desc}")
    else:
        speak("Sorry, I couldn't find the weather for that city")
