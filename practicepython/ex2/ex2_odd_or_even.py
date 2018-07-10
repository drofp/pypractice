#!/usr/bin/env python3

"""Example 2 from https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
==========================
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

def main():
    dividend, divisor = list(map(int, input("Enter two integers, separated by a space\n").split()))
    if dividend % divisor == 0:
        print("The second number evenly divides the first number!")
    else:
        print("The second number does NOT evenly divides the first number!")

if __name__ == "__main__":
    main()
