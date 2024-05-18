import pyttsx3
import speech_recognition as sr
import datetime
import os



# Taking Voice form the user

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')

# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 165)


# speak function

def speak(text):
    """This Function Takes Text And Returns Voice"""
    engine.say(text)
    engine.runAndWait()

# Speech Recognition Function

def takeCommand():
    """This function will recogzine voice and returns text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}")


        except Exception as e:
            print("Say that again please")
            return "None"
        return query

#The function for wish me by using time
def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir. How are you doing")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon sir. How are you doing")

    else:
        speak("Good evening sir. How are you doing")
    
    speak("I am Your assistant. Tell me sir how can i help you")
    

