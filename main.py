# import colorgram
# colors = colorgram.extract("image.jpg", 30)
# rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb.append(new_color)
# print(rgb)
import random
import turtle as t
from turtle import Screen
timmy = t.Turtle()
t.colormode(255)
color_list = [ (231, 206, 85), (224, 150, 89), (120, 166, 185), (159, 14, 21), (34, 110, 157), (232, 82, 46), (124, 176, 144), (8, 97, 38), (171, 21, 16), (199, 65, 28), (185, 186, 27), (31, 128, 47), (12, 41, 74), (15, 63, 40), (242, 202, 5), (138, 82, 95), (85, 15, 22), (51, 166, 77), (44, 26, 22), (6, 65, 137), (173, 135, 149), (232, 170, 160), (48, 150, 195), (219, 66, 71), (74, 135, 186), (169, 206, 175)]
timmy.hideturtle()
x = -250
y = -250
timmy.teleport(x, y)
while y < 250:
    for i in range(10):
        color = random.choice(color_list)
        timmy.color(color)
        timmy.dot(20)
        timmy.up()
        timmy.forward(50)
        timmy.down()
    y += 50
    timmy.teleport(x, y)

my_screen = Screen()
my_screen.exitonclick()