import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("circle")
tim.shapesize(1)

turtle.colormode(255)
colour = ["red", "chartreuse3", "DarkOliveGreen", "DarkMagenta", "brown2", "blue1", "cyan", "DeepPink2", "BlueViolet",
          "LightSkyBlue", "NavajoWhite3", "Gold", "midnightblue"]

# end = False
# start = 2
# while not end:
#     start += 1
#     tim.color(random.choice(colour)),
#     tim.fillcolor(random.choice(colour))
#     for number in range(start):
#         tim.forward(100)
#         tim.right(360/start)
#     if start == 10:
#         end = True


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_colours = (r, g, b)
    return my_colours


tim.pensize(1)
tim.speed(6)
# angles = [0, 90, 180, 270]
angle = 0

# for _ in range(300):
#     tim.color(random_colour()),
#     tim.fillcolor(random_colour())
#     tim.seth(random.choice(angles))
#     tim.forward(30)

for _ in range(180):
    tim.tilt(angle)
    tim.color(random_colour())
    tim.fillcolor(random_colour())
    # tim.seth(random.choice(angles))
    tim.circle(-100)
    angle += 30



# end = False
# counter = 0
# while not end:
#     counter += 1
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     if counter == 15:
#         end = True

screen = Screen()
screen.exitonclick()
