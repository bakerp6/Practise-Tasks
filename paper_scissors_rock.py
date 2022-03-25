"""This is the traditional game of Paper, Scissors, Rock designed for one player
to play against the computer. The program gets the players name and then starts
the first game. The first to win 3 games wins the round. Scores are shown at the
end of each game as well as the end of each round. At the end of each
round the player is also asked if they want to play another round or quit.
The program keeps offering a new round until the player quits.

Created by Patrick Baker
7th June 2021
"""


import random  # Need to import this to get the computer choice


# This is the main game playing function
def play_game(named):
    player_name = named
    player_score = 0
    computer_score = 0

    choices = ["Paper", "Scissors", "Rock"] # List of possible choices

    # Welcome below neatly set out using line breaks and tab spacing
    print(f"\nHi {player_name}\n\tP = Paper\n\tS = Scissors\n\tR = Rock\n")
    while player_score < 3 and computer_score < 3:  # Game ends as soon as one
        # score gets to 3

        computer = random.choice(choices)  # This is a method of making a
        # random choice from a list

        player = get_player_choice()  # Player's choice is obtained from its
        # own function

        # The line below calculates the 3 conditions needed for a player  win
        if player == "Paper" and computer == "Rock" or player == "Scissors" and\
                computer == "Paper" or player == "Rock" and \
                computer == "Scissors":

            player_score += 1  # Awarding the player a point for a win
            congratulations(player_name, player_score, computer_score)

        elif player == computer:  # Need to account for draws next
            print("\nThat's a draw. Try again.")
            print(f"\tYour score is still {player_score} and \n\tmy score "
                  f"remains at {computer_score}\n")

        else:  # In all other cases the computer wins
            computer_score += 1
            commiserations(player_name, player_score, computer_score)

    # The line below only gets used when one of the scores gets to 3 and breaks
    # the loop above
    calculate_result(player_name, player_score, computer_score)


# This function gets the player's choice - using the first letter (minimising
# player entry errors)
def get_player_choice():
    choice = input("Enter your choice - 'P' or 'R' or 'S': ").upper()

    # Checks to make sure the choice is ONLY one of the allowed options
    while choice != "P" and choice != "R" and choice != "S":
        choice = input("Choice can only be 'P' or 'R' or 'S': ").upper()

    # Converts the first letter in the full word and returns the converted
    # value to the play_game function
    if choice == "P":
        return "Paper"
    elif choice == "R":
        return "Rock"
    else:
        return "Scissors"


# This function is used when the player wins
def congratulations(player_name, player_score, computer_score):
    print(f"\nCongratulations {player_name}. "
          f"You won that round\n\tYour score is currently {player_score}\n\t"
          f"My score is currently {computer_score}\n")


# This function is used when the player loses
def commiserations(player_name, player_score, computer_score):
    print(f"\nBad luck {player_name}. "
          f"You lost that round\n\tYour score is currently {player_score}\n\t"
          f"My score is currently {computer_score}\n")


# This function is used at the end of each match
# -when one player has won 3 games
def calculate_result(player_name, player_score, computer_score):
    print("*" * 50)
    if player_score > computer_score:
        print(f"\nWell done {player_name}. You won the match\n\tYour final "
              f"score is {player_score}\n\tMy final score is {computer_score}")
    else:
        print(f"\nToo bad {player_name}. You lost the match\n\tYour final "
              f"score is {player_score}\n\tMy final score is {computer_score}")

    # The lines below ask the player if they want another turn
    end_play = input("\nPress <enter> to play again "
                     "or any other key and <enter> to quit")
    if not end_play:
        play_game(player_name) # Pushing <enter> with any other key will give
        # 'end_play' a value and go back to the main routine


# Main routine
print()
print("*" * 50)
print("\nThis is a game of Paper, Scissors, and Rock.\nYou make your choice "
      "and the computer makes a choice. \nThe winner is decided as follows:\n"
      "\n\tPaper beats Rock\n\tScissors beats Paper\n\tRock beats Scissors\n")
name = input("What is your name? ").title()
play_game(name)  # This function runs the program until the user wants to quit
print("\nGoodbye. Thanks for playing :)")

