import turtle
import random
t = turtle.Turtle()
t.shape("classic")

t.up()
t.goto(0, 300)
t.down()

n = int(input("몇각형 (숫자입력) : "))
s = int(input("선 길이 (숫자입력) : "))
sp = int(input("그리는 속도 (숫자입력) : "))

t.speed(sp)
color = ["#abffab", "#ffabff", "#abff00", "red", "gold", "skyblue", "silver", "green"]
for i in range(n) :
    t.color(color[random.randint(0, 7)])
    t.width(random.randint(1, i+1))
    t.fd(s)
    t.right(360/n)

t.up()
t.goto(0, 0)
t.down()

for i in range(100) :
    t.color(color[random.randint(0, 7)])
    t.width(random.randint(1, i+1))
    t.fd(s)
    t.rt(random.randint(-360, 360))

end = input()