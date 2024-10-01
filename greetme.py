import pyttsx3
import  datetime

engine=pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",70)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 or hour<=12:
        speak("good morning  ")
    elif hour>12 and  hour<=18:
        speak(" good afternoon")

    else:
        speak("good evening ")
    speak("please tell me how can i help u ?")

    



