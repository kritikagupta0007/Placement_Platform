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
    engine.endLoop()
    engine.stop()
    

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
    if 'Hello' in command:
        say('Hello how can I help You')
    if 'help' in command:
        say('yes,I am here for your help tell me how can I help you')
    if 'company' in command:
        say('So many companies came there for the placement may be approx 50 to 60 companies')
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
               
def start_chat(request):
    # say('Welcome to the placment Smart chat, I am here for your help, Please tell me how can i help you')
    while True:
        run_alexa()
        return render(request, 'chat.html')

def chat(request):
    return render(request, 'chat.html')





# from tkinter import *

# root = Tk()

# def send():
#     send = "You:"+ e.get()
#     text.insert(END,"\n" + send)
#     if(e.get()=='hi'):
#         text.insert(END, "\n" + "Bot: hello")
#     elif(e.get()=='hello'):
#         text.insert(END, "\n" + "Bot: hi")
#     elif (e.get() == 'how are you?'):
#         text.insert(END, "\n" + "Bot: i'm fine and you?")
#     elif (e.get() == "i'm fine too"):
#         text.insert(END, "\n" + "Bot: nice to hear that")
#     else:
#         text.insert(END, "\n" + "Bot: Sorry I didnt get it.")
# text = Text(root,bg='light blue')
# text.grid(row=0,column=0,columnspan=2)
# e = Entry(root,width=80)
# send = Button(root,text='Send',bg='blue',width=20,command=send).grid(row=1,column=1)
# e.grid(row=1,column=0)

# root.title('IT SOURCCODE SIMPLE CHATBOT')
# root.mainloop()