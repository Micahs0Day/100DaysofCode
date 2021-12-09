import random
import turtle

""" Turtle Method/attribute declarations"""
crush = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
crush.penup()
crush.hideturtle()
crush.speed("fastest")

""" RGB Color pallete that was created from spots.jpg """
color_list = [(24, 24, 49), (242, 219, 68), (238, 173, 45), (246, 239, 214), (49, 13, 31),
              (243, 32, 49), (149, 21, 39), (158, 92, 31), (61, 84, 111), (19, 44, 30),
              (48, 45, 106), (203, 165, 20), (49, 189, 95), (57, 114, 83), (228, 242, 229),
              (131, 192, 141), (185, 240, 4), (50, 22, 10), (170, 49, 72), (155, 215, 142)]


""" Crush(Turtle Obj) starting cooridinates """

def painting():
    x = -250
    y = -250
    crush.setposition(x, y)
    while y < 250:
        x +=50
        crush.setposition(x, y)
        crush.dot(20, random.choice(color_list))
        if x == 250:
            x = -250
            y += 50
        if y >= 250:
            return

painting()

screen.exitonclick()
