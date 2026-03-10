# 太阳花绘制
import turtle

t = turtle.Turtle()
t.color("red", "yellow")
t.speed(10)

t.begin_fill()
for i in range(36):
    t.forward(200)
    t.left(170)
t.end_fill()

turtle.done()