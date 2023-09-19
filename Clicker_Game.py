import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import random
import time
import pygame
from PIL import ImageTk, Image, ImageOps
import sys, os
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

tk = Tk()

tk.geometry("800x500")

tk.title("Smurfcat clicker")

clicks = 0

tk.configure(background="black")


clicklabel = Label(text= clicks, font= "Arial, 16")

clicklabel.pack(pady= 20)

messagebox.showinfo("Clicker Game", "Welcome to the Clicker Game")

pygame.mixer.init()

enableclicksper = 0

eanble5xclick = 0
img = Image.open(os.path.join(application_path, "smurfcat.jpeg"))


rezised_image = ImageOps.contain(img, (100,50))
photo = ImageTk.PhotoImage(rezised_image)

def playsound():
    pygame.mixer.music.load(os.path.join(application_path, "mouseclick.mp3"))
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(2)


def randomize():
    global clicks
    if clicks >= 200:
        clicks -= 200
        clicks += random.randint(1,400)
        clicklabel.config(text=clicks)
        playsound()
    
    else:
        messagebox.showinfo("clicker game", "not enough clicks you need 200 clicks")
    
def background_music():
    pygame.mixer.music.load(os.path.join(application_path,"elevator_music.mp3"))
    pygame.mixer.music.play(loops= True)
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(os.path.join(application_path,"elevator_music.mp3")))

background_music()

def double_click():
    global clicks
    global eanble5xclick
    if clicks >= 1000:
        eanble5xclick += 1
        clicks -= 1000
        messagebox.showinfo("clicker game", "You have now unlocked 5 clicks per click!")
    elif eanble5xclick >= 1:
        eanble5xclick == 1
    else:
        messagebox.showinfo("clicker game", "not enough clicks you need 1000 clicks")

    

def loopclicks():
    global clicks
    tk.after(1000, loopclicks)
    clicks += 10
    clicklabel.config(text=clicks)

def onclickseconde():
    global enableclicksper
    global clicks
    if clicks >= 400:
        clicks -= 400
        playsound()

        enableclicksper += 1
    if enableclicksper == 1:
        messagebox.showinfo("clicker game", "You have now unlocked 10 clicks per second!")
        tk.after(0, loopclicks)
    else:
        messagebox.showinfo("clicker game", "not enough clicks you need 400 clicks")


def onClick():
    global eanble5xclick
    global clicks
    clicks += 1
    print(clicks)
    clicklabel.config(text=clicks)
    playsound()
    if eanble5xclick == 1:
        clicks += 4



cps = ttk.Button (tk,text="Click per second", command= onclickseconde,width = 20)
cps.pack(ipady=20)

more_click = ttk.Button(tk,text="5x Click",command= double_click, width = 20)
more_click.pack()


button = ttk.Button(tk,command=onClick , width = 50, image = photo)
button.pack(padx=100,ipadx=100 ,ipady=75,)#Ipady står for internal padding

ranodom_button = ttk.Button(tk,text="Randomize",command=randomize, width= 25)
ranodom_button.pack(padx=100,ipady = 75)

tk.mainloop()



    


