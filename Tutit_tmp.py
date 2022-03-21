import turtle as t
import random

def screenLeftClick(x,y):
    tSize = random.randrange(2,10)
    t.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    t.color((r,g,b))
    tAngle = random.randrange(0,360)

    t.penup()
    t.goto(x,y)
    t.left(tAngle)
    t.stamp()

t.shape("turtle")
t.setup(600,400)
t.onscreenclick(screenLeftClick,1)
t.done()