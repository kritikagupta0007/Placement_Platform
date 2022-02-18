from django.shortcuts import render

# Create your views here.
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener = sr.Recognizer()
mic = sr.Microphone()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def say(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with mic as source :
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
        print('Recoginizing...')
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '')
            # say(command)
            # print("hi")
            # print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    #print("Hello")
    if 'play' in command:
        song = command.replace('play', '')
        say("playing"+ song )
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        say('Current time is' + time)
        print(time)
    elif 'are you single' in command:
        say('i am in relationship with wifi')
    elif 'date' in command:
        say("I'll go anywhere you take me")
    elif 'beautiful' in command:
        say('wow thanks. i think you are beautiful too')
    elif 'free fire' in command:
        say('no , i am very busy with my work')
    elif 'joke' in command:
        say('A ham sandwich walks into a bar and orders a beer, bartender says “sorry, we don’t serve food here.”')
    else:
        say('sorry i can not get it. please repeat the command again')

run_alexa()       