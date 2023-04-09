from turtle import Turtle, Screen
import random as rand

turtle_list = []
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()

# store = screen.numinput("This is Title", "How many types of egg do you like?", default=10, minval=1, maxval=50)
# print(store)
screen.setup(width=500, height=400)
screen.title(titlestring='Turtle Race')
y_position = 100
for turtle_index in range(6):
    turtle = Turtle(shape='turtle')
    turtle.color(colours[turtle_index])
    turtle.penup()
    turtle.setposition(x=-225, y=y_position)
    y_position -= 40
    turtle_list.append(turtle)

user_turtle = screen.textinput("Make your bet", "Who will win the race? Enter a colour:").lower()

game_finish = False
while not game_finish:
    for turtle in turtle_list:
        move = rand.randint(0, 10)
        turtle.forward(move)
        if turtle.xcor() > 225:
            winning_color = turtle.pencolor()
            game_finish = True

            writer = Turtle()
            writer.hideturtle()
            writer.penup()
            writer.goto(x=0, y=175)
            if winning_color == user_turtle:
                # print(f"You've won! The {winning_color} turtle is the winner.")
                writer.write(f"You've won! The {winning_color} turtle is the winner.", align="center")
            else:
                # print(f"You've lost! The {winning_color} turtle is the winner.")
                writer.write(f"You've lost! The {winning_color} turtle is the winner.", align="center")
            break

screen.exitonclick()
