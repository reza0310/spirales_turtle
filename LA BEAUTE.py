#-------------------------------------------------------------------------------
import turtle
from random import *
turtle.pendown()
turtle.speed(0)
turtle.colormode(cmode = 255)
color = [0, 0, 0]
for i in range(1, 300):
    turtle.width(int(i/10))
    turtle.pencolor(color)
    color = (randint(0, 255), randint(0, 255), randint(0, 255))

    turtle.circle(i, 1000)