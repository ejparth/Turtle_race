# A turtle race game!!
# one can learn how to create multiplayers, different objects, and how to add functionality to different objects
from turtle import Turtle, Screen
import random

# making a screen instance from a screen class
screen = Screen()

# setup the screen width and size
screen.setup(width=500, height=400)
user_a = screen.textinput(title="Make  your bet", prompt="who will win?")
print(f"you entered {user_a}")

# for different turtles
y_pos = [-70, -40, -10, 20, 50, 80]
colors = ["red", "yellow", "orange", "green", "blue", "cyan"]
all_turtle = []

# creating turtles and moving them to starting pos
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtle.append(new_turtle)

# setting condition to stop while loop
game_flag = True
if user_a:
    game_flag = False

while not game_flag:
    for turtle in all_turtle:  # this loop go in one by one to all the turtle objects and ask them to do task
        if turtle.xcor() > 220:
            game_flag = True  # exit the loop if anyone reached the finishline(i.e. the boundary of screen)
            if user_a == turtle.pencolor():
                print(f"You won got {user_a} as winner")
            else:
                print(f"you lost!, as {turtle.pencolor()} is winner")
        a = random.randint(0, 10)
        turtle.forward(a)

screen.exitonclick()
