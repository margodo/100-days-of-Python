import idlelib.tree
import turtle
import pandas
screen = turtle.Screen()
screen.title("US States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed = []
states = pandas.read_csv("50_states.csv")
states_list = states['state'].to_list()
while len(guessed) < 50:
    answer = screen.textinput(f"{len(guessed)}/50. Guess the state", "Pleas enter state's name:")
    if answer.title() in states_list:
        name_state = turtle.Turtle()
        name_state.hideturtle()
        name_state.penup()
        data = states[states.state == answer.title()]
        name_state.goto(data.x.item(),data.y.item())
        name_state.write(data.state.item())
        guessed.append(answer)
    if answer.lower() == "exit":
        missing = [i for i in states_list if i not in guessed]
        # for i in states_list:
        #     if i not in guessed:
        #         missing.append(i)
        new_data = pandas.DataFrame(missing)
        new_data.to_csv('states_to_learn.csv')
        break