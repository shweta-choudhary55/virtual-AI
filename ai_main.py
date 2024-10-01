import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup 
import datetime
import os

engine=pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",70)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r =speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=300
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source,0,4)
        

    try:
        print("understanding..")
        query =r.recognize_google(audio,language='en-in')
        print(f"you said:{query}\n")

    except Exception as e:
        print("say that again")
        return "None"
    return query

def alarm(query):
    timehere=open("alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")



if __name__=="__main__":
    while True:
        query =takecommand().lower()
        if "wake up" in query:
            from greetme import greetMe
            greetMe()

            while True:
                query =takecommand().lower()
                if "go to sleep" in query:
                    speak("ok , you can call me anytime")
                    break
                elif "hello" in query:
                    speak(" hello , how are you?")
                elif "i am good " in query:
                    speak("that's great")

                elif " how are you " in query:
                    speak("perfectly fine ")
                elif "thank you " in query:
                    speak("you are welcome ")

                elif "open" in query:
                    from dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from dictapp import closeappweb
                    closeappweb(query)
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("set the time ")
                    a= input("please tell the time:-")
                    alarm(a)
                    speak("done")

                elif "google" in query:
                    from searchnow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query :
                    from searchnow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from searchnow import searchwikipedia
                    searchwikipedia(query)
                elif "temperature" in query:
                    search="temperature in delhi"
                    url=f"https://www.google.com/search?q={search}"
                    r=requests.get(url)
                    data= BeautifulSoup(r.text,"html.parser")
                    temp=data.find("div", class_ = "BNeawe").text
                    speak(f"Current {search} is {temp}")
                    
                    


                elif "weather" in query:
                    search="weather in delhi"
                    url=f"https://www.google.com/search?q={search}"
                    r=requests.get(url)
                    data= BeautifulSoup(r.text,"html.parser")
                    temp=data.find("div", class_ = "BNeawe").text
                    speak(f"Current {search} is {temp}")

                elif " what is the time" in query:
                    strTime= datetime.datetime.now().strftime("%H:%:M")
                    speak(f"the time is{strTime}")

                elif "finally sleep" in query:
                    speak("going to sleep")
                    exit()



                    
   




      

    