#!usr/bin/env python3

"""Example 8 from https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
==========================
- Two player rock, paper, scissors game. 

- Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, and ask if the players want to start a new game 
"""

def declare_hand():
    """Prompt users for input, informs if input is invalid"""

    validHandChosen = False

    while validHandChosen is False:
        player1Choice = input("\n======Player 1 - Choose your hand!======\n" +
                              "Choices are: 'Rock', 'Paper', or 'Scissors'" +
                          "\n--> ")
        if is_valid(player1Choice):
            # print("Player 1 chooses:", player1Choice)
            validHandChosen = True

    validHandChosen = False

    while validHandChosen is False:
        player2Choice = input("\n======Player 2 - Choose your hand!======\n" +
                              "Choices are: 'Rock', 'Paper', or 'Scissors'" + 
                              "--> ")
        if is_valid(player2Choice):
            # print("Player 2 chooses:", player2Choice)
            validHandChosen = True

    return player1Choice, player2Choice

def is_valid(chosenHand):
    """Check if hand is valid"""

    if chosenHand == "Rock" or chosenHand == "Paper" or chosenHand == "Scissors":
        return True

    print("Invalid hand! Please Choose from one of the following:\n" +
          "'Rock', 'Paper', or 'Scissors'")
    return False

def decide_winner(player1Choice, player2Choice):
    """Decides who wins the round.
    Assumes that inputs are either 'Rock', 'Paper', 'Scissors'"""
    
    if player1Choice == "Rock":
        if player2Choice == "Scissors":
            return "Player 1"
        elif player2Choice == "Paper":
            return "Player 2"
        elif player2Choice == "Rock":
            return "It's a Tie"
    elif player1Choice == "Paper":
        if player2Choice == "Rock":
            return "Player 1"
        elif player2Choice == "Scissors":
            return "Player 2"
        elif player2Choice == "Paper":
            return "It's a Tie"
    elif player1Choice == "Scissors":
        if player2Choice == "Paper":
            return "Player 1"
        elif player2Choice == "Rock":
            return "Player 2"
        elif player2Choice == "Scissors":
            return "It's a Tie"

def play_one_game():
    player1Choice, player2Choice = declare_hand()
    winner = decide_winner(player1Choice, player2Choice)

    print("The winner is: {}!".format(winner))

def prompt_new_game():
    validPlayAgainChoice = False
    
    while validPlayAgainChoice == False:
        playAgainChoice = input("\nWould you like to play another game? [y/n]\n" +
                                "--> ")

        if playAgainChoice == "y":
            print("===========================\n" +
                  "Now loading another game...\n" +
                  "===========================\n")
            return True
        elif playAgainChoice == "n":
            print("==================================\n" +
                  "Thanks for playing! now exiting...\n" +
                  "==================================\n")
            return False
        else:
            print("Please enter either 'y' or 'n'...")

def main():
    keepPlaying = True

    while keepPlaying == True:
        play_one_game()
        keepPlaying = prompt_new_game()

    
if __name__ == "__main__":
    main()



