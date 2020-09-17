from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
from threading import Thread
import pyttsx3 as pp
import speech_recognition as s
from PIL import ImageTk,Image


engine=pp.init()
voices = engine.getProperty('voices')
print(voices)

# Set voice male or female '0' contain male voice and '1' contain female voice

engine.setProperty('voice',voices[1].id)

# For speek audio create a function
def speak(word):
    engine.say(word)
    engine.runAndWait()
# ptttsx2 instal library for voice
bot = ChatBot('Manir')


# for boat training
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
trainer = ListTrainer(bot)

#now training the bot with the help of trainer

trainer.train(conversation)



#For testing purposes use

#answer = bot.get_response("How are you doing?")
#print(answer)

# print("Talk To super bot")
# while True:
#     query=input()
#     if query == 'exit':
#         break
#     answer=bot.get_response(query)
#     print("bot : ", answer)


# Creating a window holp tkinter for conversation
main = Tk()

main.geometry("400x700")
# main.iconbitmap()
main.title("My Super Chat bot")
my_img = ImageTk.PhotoImage(Image.open("OIP.png"))
my_label = Label(image=my_img)
my_label.pack()


# photo = PhotoImage(file='C:\\Users\kmani\OneDrive\Desktop\OIP.png')
# photoL = Label(main, image=photo)
# photoL.pack()

# take query :takes audio as input from user and convert it to string
def takeQuery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("Your bot is listening")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio,language='eng-in')
            print(query)
            textF.insert(0,END)
            textF.insert(0,query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")
# Creating functin for bot responese
def ask_from_bot():
    query = textF.get()
    answer = bot.get_response(query)
    msgs.insert(END, "You : "+ query)
    msgs.insert(END, "Super Bot : "+ str(answer))
    speak(answer)
    textF.delete(0,END)

    # scroll bar work properly
    msgs.yview(END)

# Create a frame for chat box
frame=Frame(main)
sc=Scrollbar(frame)
msgs= Listbox(frame, width=80,height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
# creating text field
textF = Entry(main,font=("Verdana",20))
textF.pack(fill=X, pady=10)
btn=Button(main,text="Send Message", font=("Verdana",20),command=ask_from_bot)
btn.pack()

# creating a function
def enter_function(event):
    btn.invoke()

# going to bind main window with Enter key
main.bind('<Return>', enter_function)


def repeatLis():
    while True:
        takeQuery()
t=Thread(target=repeatLis)
t.start()

main.mainloop()
