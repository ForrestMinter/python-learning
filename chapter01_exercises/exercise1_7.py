# 五角星绘制
import turtle

t = turtle.Turtle()
t.color("red")
t.pensize(2)

for i in range(5):
    t.forward(100)
    t.right(144)  # 五角星的角度

turtle.done()  # 保持窗口