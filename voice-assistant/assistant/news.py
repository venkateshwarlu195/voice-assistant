import requests
from assistant.speech import speak

API_KEY = "YOUR_NEWS_API_KEY"

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"
    data = requests.get(url).json()

    articles = data.get("articles", [])[:5]
    if not articles:
        speak("Sorry, I couldn't fetch the news")
        return

    speak("Here are the top headlines")
    for article in articles:
        speak(article["title"])
