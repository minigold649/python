import random
import turtle
r = random
t = turtle.Pen()

a = 80
sp = 1
t.width(5)
while(True):
    n = r.randint(1, 3)
    t.clear()
    t.up()
    t.speed(100)
    if(n == 1):
        t.speed(sp*2)
        t.goto(0, 100)
        t.down()
        t.right(90)
        t.forward(200)
        t.goto(0, 100)
        t.right(45)
        t.forward(50)
        t.left(135)
        t.up()
        t.goto(-40, -100)
        t.down()
        t.forward(80)
        for i in range(0, a):
            t.speed(1)
            t.up()
            t.forward(-1)
    elif(n == 2):
        t.goto(-50, 100)
        t.down()
        t.left(90)
        t.speed(sp*5)
        for i in range(0, 11):
            t.right(20)
            t.forward(20)
        t.speed(sp*2)
        t.forward(140)
        t.left(130)
        t.forward(120)
        for i in range(0, a):
            t.speed(1)
            t.up()
            t.forward(-1)
    elif(n >= 3):
        t.speed(sp*5)
        t.up()
        t.goto(-50, 100)
        t.down()
        t.left(50)
        for i in range(0, 11):
            t.right(20)
            t.forward(20)
        t.left(180)
        for i in range(0, 11):
            t.right(20)
            t.forward(20)
        t.left(210)
        for i in range(0, a):
            t.speed(1)
            t.up()
            t.forward(-1)