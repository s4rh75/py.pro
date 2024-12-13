from tkinter import*
from gtts import gTTS
from playsound import playsound
import os

def play_text():
    text1=entry.get()
    tts = gTTS(text=text1, lang='en')
    tts.save("output.mp3")  
    playsound("output.mp3")
    os.remove("output.mp3")
    
def set_text():
    entry.delete(0, 'end')   

def exit_app():
    root.destroy()

root=Tk()

root.geometry("400x300")

mylabel=Label(root,text="TEXT TO SPEECH",bg="white",fg="purple").pack(pady=30)

mylabel2=Label(root,text="Enter your text",bg="white",fg="purple").pack(pady=20)

entry=Entry(root,width=40)
entry.pack()

play=Button(root,text="Play",command=play_text,bg="purple",fg="white").pack(padx=40,pady=5,ipadx=10,side=LEFT)

set=Button(root,text="Set",command=set_text,bg="purple",fg="white").pack(padx=50,pady=5,ipadx=10,side=LEFT)

exit=Button(root,text="Exit",command=exit_app,bg="purple",fg="white").pack(padx=40,pady=5,ipadx=20,side=LEFT)

root.configure(bg="lightcoral")
root.title("text to speech")
 

root.mainloop()