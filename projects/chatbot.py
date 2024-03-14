import datetime

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
def user_commands():
    command = ""
    try:
        with sr.Microphone() as source:
            print('start Speaking!')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command
def run_alexa():
    command=user_commands()
    if 'play' in command:
        song=command.replace('play','')
        engine_talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M%p')
        engine_talk("The current time is "+time)
    elif 'who is' in command:
        name=command.replace('who is','')
        info=wikipedia.summary(name,1)
        engine_talk(info)
    elif 'joke' in command:
        engine_talk(pyjokes.get_joke())
    else:
        engine_talk('I could not hear you properly')
run_alexa()



