from pgzhelper import *
from random import randint


TITLE = 'Flappy Turd'
WIDTH = 475
HEIGHT = 700

turd = Actor("turd")
turd.scale = .2 

pipe = Actor("pipe")
pipe.scale = .5


#set up game variables
gravity = 0.3
turd.speed = 1 
turd.alive = True


def draw():
    screen.fill("blue")
    turd.draw()
   #pipe.draw()


def update():
    turd.y += turd.speed
    turd.speed += gravity
    if turd.y > HEIGHT or turd.y < 0:
        turd.alive = False 
        

def on_key_up(key):
    if key == keys.SPACE and turd.alive:
        turd.speed = -6.5

# def on_mouse_down():
#     if turd.alive:
#         turd.speed = -6.5
    #if key == keys.SPACE:
        # print("pressed space!")
        # turd.y = turd.y - 50
    #    animate(turd, tween="decelerate", pos=(turd.x, turd.y - 100))

