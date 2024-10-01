import requests
import json
import pyttsx3


engine=pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",70)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict= {"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=5a87f560e399481c9cf593e7cacc9802",
             "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=5a87f560e399481c9cf593e7cacc9802",
             "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=5a87f560e399481c9cf593e7cacc9802",
             "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=5a87f560e399481c9cf593e7cacc9802",
             "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=5a87f560e399481c9cf593e7cacc9802",
             "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=5a87f560e399481c9cf593e7cacc9802"}
    
    content=None
    url=None
    speak("which field do you want ,[business],[entertainment],[health],[science],[sports],[technology]")
    field =input("Type field news that you want:")
    for key , value in api_dict.items.lower():
        if key.lower() in field.lower():
            url=value
            print(url)
            break
        else:
            url=True
    if url is True:
        print("url not found ")
    news=requests.get(url).text
    news=json.loads(news)
    speak("here is the first news.")

    arts=news["articles"]
    for articles in arts:
        article=articles["titles"]
        print(article)
        speak(article)
        news_url =articles["url"]
        print(f"for more info visit:{news_url}")

        a= input("[press 1 to cont] and [press 2 to stop]")
        if str(a)=="1":
            pass
        elif str(a)=="2":
            break
    speak("thats all")
latestnews()




