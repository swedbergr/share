# Import libraries
import random


def main():
    '''
    Main function that runs the sequencing of the game.
    '''
    # Get computer's choice
    computer_play = get_computer_play()

    # Get user's choice
    user_play = get_user_play()

    # Determine the winner
    winner = check_winner(user_play, computer_play)

    # Display the winner results
    if winner == "You win!":
        print(f"{user_play} beats {computer_play}")
    elif winner == "The computer wins!":
        print(f"{computer_play} beats {user_play}")
    else:
        print(f"{user_play} matches {computer_play}")

    print(winner)
        


def get_user_play():
    '''
    Value-returing fucntion that gets and validates the user's choice of rock, paper, or scissors.
    return: string of user's choice of rock, paper, or scissors
    '''
    # Get user choice for play
    play = input("Please select rock, paper, or scissors: ")

    # Loop to validate input
    while play != "rock" and play != "paper" and play != "scissors":
        print("That is not a valid option.")
        play = input("Please select rock, paper, or scissors: ")

    # Return user's play
    return play



def get_computer_play():
    '''
    Value-returning function that gets a random selection of rock, paper, or scissors.
    return: string of random selection of rock, paper, or scissors
    '''
    # Get random number from 3 options
    num = random.randint(0, 3)

    # Convert number to play
    play = ""
    if num == 0:
        play = "rock"
    elif num == 1:
        play = "paper"
    else:
        play = "scissors"

    # Return play for computer
    return play



def check_winner(user, computer):
    '''
    Value-returning function that takes the user and the computer's selection and determines the winner.
    param user: string for user's choice
    param computer: string for computer's choice
    return: string identifying the winner
    '''
    # Define variable for winner
    winner = ""

    # Check all conditions when user selects rock
    if user == "rock":
        # Check computer
        if computer == "rock":
            # rock ties with rock
            winner = "The game is a tie."
        elif computer == "paper":
            # paper beats rock
            winner = "The computer wins!"
        else:
            # rock beats scissors
            winner = "You win!"
    elif user == "paper":
        # Check computer
        if computer == "paper":
            # paper ties with paper
            winner = "The game is a tie."
        elif computer == "rock":
            # paper beats rock
            winner = "You win!"
        else:
            # scissors beats paper
            winner = "The computer wins!"
    else:
        # User selects scissors
        # Check computer
        if computer == "scissors":
            # scissors ties with scissors 
            winner = "The game is a tie."
        elif computer == "rock":
            # rock beats scissors
            winner = "The computer wins!"
        else:
            # scissors beat paper
            winner = "You win!"

    # Return winner rusult
    return winner
        


# Conditionally execute main()
if __name__ == "__main__":
    main()


