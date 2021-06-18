from tkinter import *
import numpy as np
from math import *
import keyboard

tk = Tk()
cnv=Canvas(tk, width=500, height=500, bg="white")
cnv.pack(padx=0, pady=0)

#-------------------------------------------------------------------------------------------------------------------------------------------
#variables initiales

#-------------------------------------------------------------------------------------------------------------------------------------------
#class

class point(object):
    def __init__(self, name):
        self.name = name
        self.x = []
        self.y = []
        self.draw = 0

player1 = point(0)
player2 = point(1)

#-------------------------------------------------------------------------------------------------------------------------------------------
#init

def init():
    cnv.create_text(250, 27, font=('Arial',50,'bold italic'), text="CHOMP GAME", fill="#e8908b")
    for i in range(5):
        for j in range(4):
            cnv.create_rectangle(50+100*i-50, 100+100*j-50, 50+100*i+50, 100+100*j+50, fill="#a1c9ea")

    cnv.create_line(0, 50, 100, 150, width=10, fill="purple")
    cnv.create_line(100, 50, 0, 150, width=10, fill="purple")

#-------------------------------------------------------------------------------------------------------------------------------------------
#draw

def draw():
    pass
    
#-------------------------------------------------------------------------------------------------------------------------------------------
#control

def control():
    if keyboard.is_pressed("r"):
        cnv.delete(ALL)
        init()

#-------------------------------------------------------------------------------------------------------------------------------------------
#first player

def firstPlayer(pos):
    if(pos.y >= 50 and pos.y <= 450):
        x = 100*int(pos.x/100)+50
        y = 100*int((50+pos.y)/100)
        cnv.create_rectangle(x-50, y-50, x+50, y+50, fill="red")

#-------------------------------------------------------------------------------------------------------------------------------------------
#second player

def secondPlayer(pos):
    if(pos.y >= 50 and pos.y <= 450):
        x = 100*int(pos.x/100)+50
        y = 100*int((50+pos.y)/100)
        cnv.create_rectangle(x-50, y-50, x+50, y+50, fill="blue")

#-------------------------------------------------------------------------------------------------------------------------------------------
#main

def main():
    tk.bind("<Button-1>", firstPlayer)
    tk.bind("<Button-3>", secondPlayer)
    control()
    draw()
    tk.after(5, main)

#-------------------------------------------------------------------------------------------------------------------------------------------

init()
main()
tk.mainloop()