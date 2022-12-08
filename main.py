import random
import turtle as turtle_m
import random as rand_
turtle_m.colormode(255)
t = turtle_m.Turtle()
t.penup()
t.speed("fast")
t.hideturtle()
colors = [(233, 222, 92), (211, 158, 105), (116, 177, 210), (226, 57, 131), (181, 78, 33), (210, 135, 174),
          (41, 103, 161), (12, 21, 62), (184, 46, 111), (186, 164, 23), (43, 182, 112)]
t.setheading(225)
t.forward(300)
t.setheading(0)
for i in range(1, 100 + 1):
    t.dot(20, rand_.choice(colors))
    t.forward(50)
    if i % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

s = turtle_m.Screen()

s.exitonclick()

# import colorgram
# colors=colorgram.extract("i.jpeg", 15)
# new_C=[]
# for ii in colors:
#     r=ii.rgb.r
#     b = ii.rgb.b
#     g = ii.rgb.g
#     c=(r,g,b)
#     new_C.append(c)
# print(new_C)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # from turtle import Turtle,Screen
# #
# # import random as r
# # t=Turtle()
# #
# # colorr=["red","orange","blue","green"]
# # t.speed(100)
# # def cir(c):
# #     for i in range(int(360/c)):
# #         t.pencolor(r.choice(colorr))
# #         t.circle(100)
# #         t.setheading(t.heading()+c)
# # cir(6)
# #
# # # t.colormode(255)
# # # def colo_r():
# # #     red=r.randint(1,255)
# # #     blue = r.randint(1, 255)
# # #     green = r.randint(1, 255)
# # #     rr=(red, blue, green)
# # #     return rr
# # # d=[0.90,180,270]
# # # for i in range(100):
# # #
# # #
# # #         t.forward(30)
# # #         t.setheading(r.choice(d))
# # #         t.color(colo_r())
# #
# #
# #
# #
# #
# # # t.forward(100)
# # # t.right(90)
# # # t.forward(100)
# # # t.right(90)
# # # t.forward(100)
# # # t.right(90)
# # # t.forward(100)
# # # t.right(90)
# #
# # """dashed line"""
# # # for i in range(10):
# # #     t.forward(10)
# # #     t.penup()
# # #     t.forward(10)
# # #     t.pendown()
# #
# # """Different shapes"""
# #
# #
# # # for i in range(3):
# # #     t.forward(100)
# # #     t.right(360/3)
# # #
# # # t.color("red")
# # # for i in range(4):
# # #     t.forward(100)
# # #     t.right(360/4)
# # #
# # # t.color("green")
# # # for i in range(5):
# # #     t.forward(100)
# # #     t.right(360/5)
# # #
# # # t.color("blue")
# # # for i in range(6):
# # #     t.forward(100)
# # #     t.right(360/6)
# # #
# # # t.color("violet")
# # #
# # # for i in range(7):
# # #     t.forward(100)
# # #     t.right(360/7)
# # #
# # # t.color("orange")
# # #
# # #
# # # for i in range(8):
# # #     t.forward(100)
# # #     t.right(360/8)
# # #
# # # t.color("maroon")
# # #
# # # for i in range(9):
# # #     t.forward(100)
# # #     t.right(360/9)
# # #
# # # t.color("maroon")
# # # for i in range(10):
# # #     t.forward(100)
# # #     t.right(360/10)
# # #
# # # t.color("maroon")
# # #
# # #
# #
# #
# # screen=Screen()
# # screen.exitonclick()
