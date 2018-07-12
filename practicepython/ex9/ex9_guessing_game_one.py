#!/usr/bin/env python3

"""Example 9 from https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
==========================
- One player guess-the-number game

- Ask player to guess a randomly chosen integer between 1 and 9 (inclusive). 
Give input on whether the guess is too low, too high, or exactly right.
- Game continues until player types "exit"
- Track number of guesses user has taken, and print this number after the game ends.
"""

import random

def play_guessing_game():
    guessMe = random.randint(1, 9)

    stillPlaying = True
    numberOfGuesses = 0

    while stillPlaying:
        currentGuess = input("Guess a number between 1 and 9 (inclusive)\n" +
                             "--> ")
        numberOfGuesses += 1

        if currentGuess == "exit":
            print("Goodbye! You tried {} times to guess the right number".format(numberOfGuesses-1))
            return
        elif int(currentGuess) == guessMe:
            print("That's correct! That only took {} tries!".format(numberOfGuesses))
            return
        elif int(currentGuess) < guessMe:
            print("A tad too low... try again!")
        elif int(currentGuess) > guessMe:
            print("A tad too high... try again!")

def main():
    play_guessing_game()

if __name__ == "__main__":
    main()
