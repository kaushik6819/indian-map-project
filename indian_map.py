import turtle
import pandas as pd
import csv


screen = turtle.Screen()
screen.title("india map game")
image = "map1.gif"
screen.setup(width=700,height=800)
screen.addshape(image)
turtle.shape(image)


df = pd.read_csv("states.csv")
all_states = df["states"].to_list()

guessed_state = []
while len(guessed_state) <=29:
    answer_seats = screen.textinput(title=f"{len(guessed_state)}/ 29 states correct     guess the state", prompt="what's another state").title()

    if answer_seats =="End":
        not_guessed =[]
        for i in all_states:
            if i not in guessed_state:
                not_guessed.append(i)
        new_data = pd.DataFrame(not_guessed)  
        new_data.to_csv("states_to_learn.csv")       
        break
        

    if answer_seats in all_states:
        if answer_seats not in guessed_state:
            guessed_state.append(answer_seats)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        staes_data = df[df["states"]== answer_seats]
        t.goto(staes_data["X"].item(),staes_data["Y"].item())
        t.write(answer_seats)
    





screen.exitonclick()
