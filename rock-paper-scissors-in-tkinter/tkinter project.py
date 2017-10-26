""""  this was created to be a show and tell at the maui makers for python class and i did not make this completely
alone i had some help from Hopsons(a youtuber) discord server this is how to read the code
L stands for label a example ls LS would be label scissors L for label S for scissors b stands for button  PI
stands for photo image P stands for photo so rockPI would be rock photo image with that out of the way lets begin"""

# imports libraries
from tkinter import *
from PIL import Image, ImageTk
import random


# creates a window in the middle of the screen 300x400 big
window = Tk()
window.geometry('350x400+750+300')


# imports. and sizes rock paper and scissor images
rockPI = Image.open("rock.png")
rockPI = rockPI.resize((100, 100), Image.ANTIALIAS)
rockP = ImageTk.PhotoImage(rockPI)
paperPI = Image.open("paper.png")
paperPI = paperPI.resize((100, 100), Image.ANTIALIAS)
paperP = ImageTk.PhotoImage(paperPI)
scissorsPI = Image.open("scissors.png")
scissorsPI = scissorsPI.resize((100, 100), Image.ANTIALIAS)
scissorsP = ImageTk.PhotoImage(scissorsPI)


# creates a frame that can be deleted
frame = Frame(window)
frame.pack()


# globals
winsNumber = 0
lossesNumber = 0
tiesNumber = 0
rock = 1
paper = 2
scissors = 3


# creates the functions

def score():
    global winsNumber
    global tiesNumber
    global lossesNumber
    score = Label(frame, text=("wins:", winsNumber, "ties:", tiesNumber, "losses:", lossesNumber))
    score.grid(row=5)


def close_window ():
    window.destroy()


def rock_input(event):
    answer = rock
    check_win(answer)


def paper_input(event):
    answer = paper
    check_win(answer)


def scissors_input(event):
    answer = scissors
    check_win(answer)


def check_win(answer):
    computer = random.randint(1, 3)

    print("computers choice was: " + str(computer))

    if answer == computer:
        you_tie()
    elif answer == rock and computer == scissors:
        you_win()
    elif answer == scissors and computer == paper:
        you_win()
    elif answer == paper and computer == rock:
        you_win()
    else:
        you_lose()


def you_win():
    global winsNumber
    winsNumber += 1
    score()


def you_lose():
    global lossesNumber
    lossesNumber += 1
    score()


def you_tie():
    global tiesNumber
    tiesNumber += 1
    score()

# creates the labels


lr = Label(frame, image=rockP)
lp = Label(frame, image=paperP)
ls = Label(frame, image=scissorsP)
l1 = Label(frame, text="lets play rock paper scissors please select rock paper or scissors")


# creates the buttons
bQuit = Button(frame, text="Quit", command=close_window)


# adds the images and labels onto the screen

l1.grid(row=0)
bQuit.grid(row=1)
lr.grid(row=2)
lp.grid(row=3)
ls.grid(row=4)


# binds the images to lefty click
lr.bind("<Button-1>", rock_input)
lp.bind("<Button-1>", paper_input)
ls.bind("<Button-1>", scissors_input)


# adds score to the screen
score()


# creates a loop so the window doesnt disappear instantly
window.mainloop()

