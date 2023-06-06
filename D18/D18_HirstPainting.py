import colorgram
import turtle as t
import random


'''
colors = colorgram.extract('image.jpg', 120)
rgb = []
for c in colors:
    rgb.append((c.rgb.r, c.rgb.g, c.rgb.b))
print(rgb)
'''

color = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58),
         (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179), (122, 169, 190), (29, 85, 93), (228, 175, 166), (181, 190, 206), (67, 77, 36), (8, 243, 241)]

turt = t.Turtle()
t.colormode(255)
turt.speed("fastest")
turt.hideturtle()
turt.penup()

y = -250
for i in range(10):
    y += 50
    x = -250
    for j in range(10):
        x += 50
        turt.setpos(x, y)
        turt.dot(20, random.choice(color))


screen = t.Screen()
screen.exitonclick()
