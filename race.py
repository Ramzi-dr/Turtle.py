#####Turtle Intro######
import turtle
from turtle import Screen, Turtle
import random
import time
screen = Screen()
screen.setup(width=600, height=500)
screen.title(titlestring= "Welcome to the turtle race ")

color = ["red", "black", "yellow", "green", "blue", "orange"]
y_position = [-90,-50, -10, 30, 70, 100]
play_again = True



while play_again:
    screen.clear()
    turtle_list = []

    for team in range(0,6):
        tim = Turtle(shape="turtle")
        tim.penup()
        tim.color(color[team])
        tim.goto(x=-270,y=y_position[team])
        tim.speed("fast")
        turtle_list.append(tim)

    user_bet = screen.textinput(title="Make ur bet",prompt="Which turtle will win the race? Enter a color:")

    if user_bet:
        race = True

        while race:
            for turtle in turtle_list:
                if turtle.xcor() < 272:
                    turtle.forward(random.randint(0,10))
                else:
                    print(turtle.pencolor())
                    winning_color = turtle.pencolor()
                    race = False
    if winning_color == user_bet:
        user_message = screen.textinput(title=f"u win the {winning_color} is the best",
                                        prompt="for replaY type 'a' for quit type 'B'").lower()

    else:
        user_message = screen.textinput(title=f"u lose the {winning_color} is the best",
                                        prompt="for replaY type 'a' for quit type 'B'").lower()
    if user_message != "a":
        play_again = False
        exit()

screen.exitonclick()
