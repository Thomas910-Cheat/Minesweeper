import tkinter as tk
from tkinter import *
import random
import os.path
import os
import sys

root = tk.Tk()
root.title("Minesweep_Kolebski_Stand:30.05.2021")

#---------------------------------------------------------------------------
#Hier sind die Einstellungen:
class Settings(object):
    #Normale Fenster Settings:
    width = 400
    height = 400
    imagewidth = 50
    imageheight = 50
    fps = 60       
    title = "Minessweep________Stand:30.05.2021" 
    bordersize = 20

    #Dateien-Standorte:
    file_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(file_path, "Image_Data")
    audio_path = os.path.join(file_path, "Audio_Data")
    
    #Farben:
    Black = (0,0,0)
    White = (255,255,255)
    Red = (255,0,0)
    Green = (0,255,0)
    Blue = (0,0,255)
time = 0
#---------------------------------------------------------------------------
#Köpfe/Buttons die eine Funktion im späteren Minesweep haben werden:
class gamebuttons:    
    #---------------------------------
    #Erste Reihe
    #---------------------------------
    btn1= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn1.grid(row=1,column=1)

    btn2= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn2.grid(row=1,column=2)

    btn3= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn3.grid(row=1,column=3)

    btn4= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn4.grid(row=1,column=4)

    btn5= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn5.grid(row=1,column=5)
    #---------------------------------
    #bg="lightblue"weite Reihe
    #---------------------------------
    btn6= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn6.grid(row=2,column=1)

    btn7= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn7.grid(row=2,column=2)

    btn8= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn8.grid(row=2,column=3)

    btn9= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn9.grid(row=2,column=4)

    btn10= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn10.grid(row=2,column=5)
    #---------------------------------
    #Dritte Reihe
    #---------------------------------
    btn11= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn11.grid(row=3,column=1)

    btn12= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn12.grid(row=3,column=2)

    btn13= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn13.grid(row=3,column=3)

    btn14= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn14.grid(row=3,column=4)

    btn15= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn15.grid(row=3,column=5)
    #---------------------------------
    #Vierte Reihe
    #---------------------------------
    btn16= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn16.grid(row=4,column=1)

    btn17= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn17.grid(row=4,column=2)

    btn18= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn18.grid(row=4,column=3)

    btn19= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn19.grid(row=4,column=4)

    btn20= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn20.grid(row=4,column=5)
    #---------------------------------
    #Fünfte Reihe
    #---------------------------------
    btn21= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn21.grid(row=5,column=1)

    btn22= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn22.grid(row=5,column=2)

    btn23= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn23.grid(row=5,column=3)

    btn24= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn24.grid(row=5,column=4)

    btn25= tk.Button(root, text=" ", height=5, width=10, bg="lightblue")
    btn25.grid(row=5,column=5)

class resetgameButton:
    def resetgame():
        root.destroy()
        os.startfile("Minesweeper_Kolebski.py")

    btnreset= tk.Button(root, text="NEW GAME", height=2, width=10,bg="grey", command=resetgame)
    btnreset.grid(row=0,column=4)

class resettime:
    def resettime():
        var = IntVar(root)
        var.set(100)
    
    btnresettime= tk.Button(root, text="RESET TIME", height=2, width=10, bg="grey")
    btnresettime.grid(row=0,column=2)

class difficulty:
    #Die Schwierigkeiten Einstellung woltte ich ursprünglich auch einfügen, habe ich aber dann letztenendes zu einem leerem Knopf ohne Funktion umgewandelt.
    btndifficultyup= tk.Button(root, text=" ", height=2, width=10,bg="grey")
    btndifficultyup.grid(row=0,column=1)

    btndifficultydown= tk.Button(root, text=" ", height=2, width=10,bg="grey")
    btndifficultydown.grid(row=0,column=5)

    def difficultybuttonlogic():
        pass

class timecount:
    def timecount():
        while root.mainloop():
            time = +1

    btnx= tk.Button(root, text=time, height=2, width=10,bg="grey")
    btnx.grid(row=0,column=3)

#---------------------------------------------------------------------------
#Hier wird die Spiellogik hinkommen:
class gamelogic:

    def newgamebuttonlogic():
        pass

    def resettimebuttonlogic():
        pass

    def difficultybuttonlogic():
        pass

#---------------------------------------------------------------------------
root.mainloop()
#Die Spiellogik ist zwar nicht so Schwer, aber ich weiß einfach nicht wie ich sie einfügen soll.