from tkinter import *
import numpy as np
from math import *
import keyboard

tk = Tk()
cnv=Canvas(tk, width=500, height=500, bg="white")
cnv.pack(padx=0, pady=0)

#-------------------------------------------------------------------------------------------------------------------------------------------
#variables initiales

player = 0
player_playing = 1

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
    global player, player_playing
    cnv.delete(player)
    if(player_playing == 1):
        player = cnv.create_text(250, 478, font=('Arial',35 ,'bold italic'), text="PLAYER 1 / GAUCHE", fill="#e8908b")
    else:
        player = cnv.create_text(250, 478, font=('Arial',35 ,'bold italic'), text="PLAYER 2 / DROITE", fill="#e8908b")

#-------------------------------------------------------------------------------------------------------------------------------------------
#control

def control():
    global player_playing
    if keyboard.is_pressed("r"):
        player_playing = 1
        cnv.delete(ALL)
        init()

#-------------------------------------------------------------------------------------------------------------------------------------------
#first player

def firstPlayer(pos):
    global player_playing
    if(pos.y >= 50 and pos.y <= 450 and player_playing == 1):
        player_playing = 2
        x = 100*int(pos.x/100)+50
        y = 100*int((50+pos.y)/100)
        cnv.create_rectangle(x-50+1, y-50+1, x+500, y+500, outline="white", fill="white")
        if(x == 50 and y == 100):
            cnv.delete(ALL)
            cnv.create_text(250, 250, font=("Arial", 45, "bold"), text="PLAYER 2 WINS", fill="#e8908b")

#-------------------------------------------------------------------------------------------------------------------------------------------
#second player

def secondPlayer(pos):
    global player_playing
    if(pos.y >= 50 and pos.y <= 450 and player_playing == 2):
        player_playing = 1
        x = 100*int(pos.x/100)+50
        y = 100*int((50+pos.y)/100)
        cnv.create_rectangle(x-50+1, y-50+1, x+500, y+500, outline="white", fill="white")
        if(x == 50 and y == 100):
            cnv.delete(ALL)
            cnv.create_text(250, 250, font=("Arial", 45, "bold"), text="PLAYER 1 WINS", fill="#e8908b")

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