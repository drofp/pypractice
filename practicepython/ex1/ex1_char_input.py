#!/usr/bin/env python3

"""Example 1 from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
==========================
Prompts user for name, age, and number of times to print. 
Prints year until user will turn age 100 in a custom message tailored to the user.
"""

import datetime

def main():
    now = datetime.datetime.now()

    name = input("Please enter your name\n")
    age = int(input("Please enter your age, in years\n"))
    multiplier = int(input("Please enter the number of times to print\n"))

    yearWillTurn100 = now.year + (100-age)
    
    outputMsg =  "Hello {}, you will be 100 in the year: {}\n".format(name, yearWillTurn100)

    print(multiplier*outputMsg)

if __name__=="__main__":
    main()
