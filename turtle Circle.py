import turtle as t

t.shape("turtle")
t.color("green")
t.speed(5)

r = int(input("몇개의 원을 그릴까요?"))

for i in range(r):
    t.circle(100)
    t.left(360/r)
    t.forward(20)

t.done()