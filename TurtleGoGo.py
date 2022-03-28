import turtle as t
import random


t.shape("turtle")
t.goto(0,0)
t. pensize(5)
t.setup(400,400)
for i in range(0,500):
    r = random.random()
    g = random.random()
    b = random.random()
    t.color((r,g,b))
    tAngle = random.randrange(0,360)
    t.forward(random.randrange(0,200))
    if t.xcor() > 200 or t.xcor() < -200 or t.ycor()>200 or t.ycor()< -200:
        t.penup()
        t.goto(0,0)
        t.pendown()
    t.left(tAngle)

t.done()
