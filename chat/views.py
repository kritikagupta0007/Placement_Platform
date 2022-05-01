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
        print(command)
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
    message = ""
    #print("Hello")
    if 'Hello' in command:
        message = 'Hello how can I help You'
    elif 'help' in command:
        message = 'yes,I am here for your help tell me how can I help you'
    elif 'company' in command:
        message = 'So many companies came there for the placement may be approx 50 to 60 companies'
    elif 'apply for internship' in command:
        message = 'Go To Internship->Choose company->Apply->Upload Resume->Done'
    elif 'view all records' in command:
        message = 'Go To Placements records'
    elif 'view all details' in command:
        message = 'Go To Placements records'
    elif 'prepare for placements' in command:
        message = 'Choose one programming course, learn it and try to solve the coding questions... All the best..!!'
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        message = 'Current time is' + time
        print(time)
    elif 'are you single' in command:
        message = 'i am in relationship with wifi'
    elif 'date' in command:
        message = "I'll go anywhere you take me"
    elif 'beautiful' in command:
        message = 'wow thanks. i think you are beautiful too'
    elif 'free fire' in command:
        message = 'no , i am very busy with my work'
    elif 'joke' in command:
        message = 'A ham sandwich walks into a bar and orders a beer, bartender says “sorry, we dont serve food here.”'
    else:
        message = 'sorry i can not get it. please repeat the command again'
    return [command, message]
               
def start_chat(request):
    while True:
        command, message = run_alexa()
        # chat = Chat
        # commands.append(command)
        # messages.append(message)
        return render(request, 'chat.html', {"command": command, "message": message})

def chat(request):
    return render(request, 'chat.html', {"command": "Command you enter will appear here...", "message": "Press speak to start chat"})





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