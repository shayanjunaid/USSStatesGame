from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.setup(height=500, width=700)
screen.title("US States Game")
screen.bgpic(picname="blank_states_img.gif")
screen.tracer(0)

states = pandas.read_csv("50_states.csv")

game_on = True
states_guessed = 0
guessed = []

while game_on:
    guess = screen.textinput(title=f"Guess a state! {states_guessed}/50", prompt="Enter guess",).title()
    if guess == "Exit":
        break
    if states[states.state == guess].empty:
        game_on = False
    else:
        turtle = Turtle(visible=False)
        turtle.penup()
        turtle.goto(int(states[states.state == guess].x), int(states[states.state == guess].y))
        turtle.write(arg=guess, align="center", font=("Arial", 8, "normal"))
        screen.update()
        states_guessed += 1
        guessed.append(guess)

allStates = states.state.to_list()
learn = [state for state in allStates if state not in guessed]

newfile = pandas.DataFrame(learn)
newfile.to_csv("States_to_Learn.csv")
screen.exitonclick()
