from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 3
BODY_PARTS = 3
SNAKE_COLOR = "#FF000"
BACKGROUND_COLOR = "#000000"


class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass

window = Tk()
window.title("Snake Game")
window.resizable(False,False)

score = 0
direction ='down'

lable = Label(window, text="score:{}".format(score),font= ('consolas',40))
lable.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()

window.update()
window_width= window.winfo_width()
window_height =window.winfo_height()
screen_width =window.winfo_screenwidth()
screen_height =window.winfo_screenheight()


x = (screen_width/2) -

window.mainloop()