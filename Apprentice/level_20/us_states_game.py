import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Apprentice/level_20/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
df = pd.read_csv("Apprentice/level_20/50_states.csv")
all_states = df.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 guessed states",
        prompt="What's another state's name?",
    ).title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_df = pd.DataFrame(missing_states)
        new_df.to_csv("Apprentice/level_20/states_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
