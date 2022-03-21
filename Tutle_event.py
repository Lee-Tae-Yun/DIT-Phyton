import turtle as t
import  random

col = ['red','yellow','green','blue','white','black','orange','pink']

def fxn(x,y):
    print("button cliked!!!")
    print('x =',x,'y =',y)
    global col
    ind = random.randint(0,7)
    t.bgcolor(col[ind])

def screenLeftClick(x,y):
    global r,g,b
    t.pencolor((r,b,g))
    r = random.random()
    g = random.random()
    b = random.random()
    t.pendown()

    t.goto(x,y)


def screenRightClick(x,y):
    t.penup()
    t.goto(x,y)

def screenMidClick(x,y):
    global r,g,b
    tSize = random.randrange(1,10)
    t.shapesize(tSize)
    t.pensize(tSize)

r,g,b = 0.0,0.0,0.0

# print(col)
# print(col[0],col[1],col[7])
# print('length =',len(col))
# print(type(col))
t.setup(600,300)
t.shape("turtle")

t.onscreenclick(screenLeftClick,1)
t.onscreenclick(screenRightClick,2)
t.onscreenclick(screenMidClick,3)


t.done()