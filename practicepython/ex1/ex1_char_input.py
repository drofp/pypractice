#!/usr/bin/env python3

"""Example 1 from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html"""

def main():
    name = input("Please enter your name\n")
    age = int(input("Please enter your age, in years\n"))

    # assuming current year is 2018
    yearWillTurn100 = 2018 + (100-age)

    print("You will be 100 in the year:", yearWillTurn100)

if __name__=="__main__":
    main()
