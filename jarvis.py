import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Lara here ,How may i help you Sir ?")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"You said : {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True :
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Opening Youtube...')
            chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome).open("youtube.com")

        elif 'open google' in query:
            speak('Opening Google...')
            chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome).open("google.com")
        
        elif 'open stack overflow' in query:
            speak('Opening stackoverflow...')
            chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome).open("stackoverflow.com")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir,the time is {strTime}")

        elif 'who are you' or 'tell me about yourself' in query:
            speak("Hi i am Lara and i'm your assistant i am made by Urmil")

        elif 'open code' in query:
            codePath = "C:\\myvscode\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


        elif 'lara quit' in query:
            speak("thanks for your time")
            break