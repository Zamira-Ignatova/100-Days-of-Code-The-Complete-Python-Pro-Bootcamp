import turtle
import  pandas

# Set up the screen and add the image
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# Read the CSV file containing US states data
states_df = pandas.read_csv("50_states.csv")
all_states_list = states_df.state.to_list()
# Initialize game variables
score = 0
game_is_on = True
# Create the turtle for displaying right answers
answer_turtle = turtle.Turtle()
answer_turtle.hideturtle()
answer_turtle.penup()
#take the user's answer and place it on the map in case it is correct
while game_is_on:
    answer = turtle.textinput(f"Guess a state {score}/{len(states_df)}",
                              prompt= "What is another state?\n"
                                      "In case you want the game finish - type 'Exit'").capitalize()
    # actions in case user wants to finish game before user guessed all the states
    if answer == "Exit":
        game_is_on = False
        answer_turtle.home()
        answer_turtle.write(f"The game has been finished\n"
                            f" The list of states you could not guessed will be saved.", align="center", 
                            font=("Arial", 24, "normal"))
        #save the states that have not been guessed into a csv
        # 1. via import csv
        # with open("Remaining_states.csv", mode = "w") as file_states:
        #     remaining_states = csv.writer(file_states)
        #     remaining_states.writerow(all_states_list)
        #2. via pandas
        remaining_states = pandas.DataFrame(all_states_list)
        remaining_states.to_csv("remaining_states.csv")
    # looping through the rows of the dataframe in order to check if the answer is there
    for row in states_df.index:
        if states_df.loc[row, "state"] == answer:
            # Get the coordinates for the state
            x_cor = int(states_df.loc[row, "x"])
            y_cor = int(states_df.loc[row, "y"])
            # Increment score
            score += 1
            # Move the turtle to the coordinates and write the state on the map
            # answer_turtle.setx(x_cor)
            # answer_turtle.sety(y_cor)
            answer_turtle.teleport(x=x_cor, y=y_cor)
            answer_turtle.write(f"{answer}")
            if answer in all_states_list:
                all_states_list.remove(answer)
        #action in case all the states have been guessed
        if score == len(states_df):
            game_is_on = False
            answer_turtle.home()
            answer_turtle.write("You have guessed them all! ")
    # Update the screen to reflect any changes
    screen.update()
