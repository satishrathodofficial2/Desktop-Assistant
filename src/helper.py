import pyttsx3
import speech_recognition as sr
import datetime
import os
import google.generativeai as genai
from gtts import gTTS



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





GOOGLE_API_KEY = "AIzaSyASi6dfYEkic-WZPPF5mTdXpO7wpFso8cY"
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY


def voice_input():
    # Create a recognizer instance
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)  # Using Google Speech Recognition
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


    

def text_to_speech(text):
    # Create a gTTS object
    tts = gTTS(text=text, lang='en')  # Language can be changed

    # Save the audio as an MP3 file
    tts.save("speech.mp3")



def llm_model_object(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    
    model = genai.GenerativeModel('gemini-pro')
    
    response=model.generate_content(user_text)
    
    result=response.text
    
    return result
    
    

