from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()


def move_forward():
    turt.forward(10)


screen.listen()
# NO Parenthesis(Brackets) after function name because we want to execute function only after key press.(For Code Below)
# When you pass one function as input to another we do Not put parenthesis at the end of the function name.
# A function which takes another function as input(in this case "onkey") is called higher order functions.
screen.onkey(fun=move_forward, key="space")

screen.exitonclick()
