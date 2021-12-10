from turtle import Turtle, Screen, onkey

crush = Turtle()
screen = Screen()


def turtle_forward():
    crush.forward(5)


def turtle_backward():
    crush.backward(5)


def turtle_left():
    crush.left(5)


def turtle_right():
    crush.right(5)


screen.onkeypress(turtle_forward, "w")

screen.onkeypress(turtle_backward, "s")

screen.onkeypress(turtle_left, "a")

screen.onkeypress(turtle_right, "d")

screen.onkey(screen.reset, "c")


screen.listen()
screen.exitonclick()

