from turtle import Turtle, Screen
import pandas
import time
FONT = ("Arial", 10, "normal")
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)
screen.tracer(0)
all_states = pandas.read_csv("50_states.csv")
answer_state = ""
gussed_states = []
title = "Guess the States"


def answer(title):
    global answer_state
    global gussed_states
    answer_state = screen.textinput(title=title, prompt="What's state's name?").capitalize()
    return answer_state


def create_word(x_coord, y_coord):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.hideturtle()
    new_turtle.pensize()
    new_turtle.goto(x_coord, y_coord)
    new_turtle.write(pos, font=FONT)


while len(gussed_states) < 50:
    screen.update()
    time.sleep(1)
    answer(title)
    if answer_state == "Exit":
        missing_state = [pos for pos in all_states["state"] if pos not in gussed_states]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn")
        break
    elif answer_state in gussed_states:
        title = f"{len(gussed_states)}/50 You already guessed it state"
    elif answer_state in all_states["state"].to_list():
        gussed_states.append(answer_state)
        title = f"{len(gussed_states)}/50 States Correct"
    else:
        title = f"{len(gussed_states)}/50 States Incorrect"

    for pos in all_states["state"]:
        if pos == answer_state:
            need_state = all_states[all_states["state"] == pos]
            x_coord = int(need_state["x"])
            y_coord = int(need_state["y"])
            create_word(x_coord, y_coord)

