import requests
import json
import time


def speak(str):
    from win32com.client import Dispatch
    bolo = Dispatch("SAPI.SpVoice")
    bolo.Speak(str)


if __name__ == '__main__':
    speak("Enter the API Key: ")
    apiKey = input("Enter the API Key: ")

    speak("About which topic you want the news of: ")
    qInTitle = input("About which topic you want the news of: ")
    speak(f"News for the topic {qInTitle} will be told by me soon.")
    qInTitle = qInTitle.replace(" ", "%20")

    url = f"https://newsapi.org/v2/everything?qInTitle={qInTitle}&language=en&apiKey={apiKey}"

    news = requests.get(url).text
    news_json = json.loads(news)

    totalResult = news_json["totalResults"]
    speak(f"The total articles I got are {totalResult}")

    arts = news_json["articles"]
    for articles in arts:
        speak(articles["title"])
        speak(articles["description"])
        time.sleep(3)
