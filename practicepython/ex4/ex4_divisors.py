#!usr/bin/env python3

"""Example 4 from https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
==========================
- Ask user for a number.

- Print a list of all integers that evenly divide into the input number
"""

def isDivisor(dividend, checkDivisor):
    if dividend % checkDivisor == 0:
        return True
    return False

def main():
    chosenNum = int(input("Please input an integer greater than 0\n" +
                          "--> "))

    print(list(currentVal for currentVal in range(1, chosenNum+1) if isDivisor(chosenNum, currentVal)))

if __name__ == "__main__":
    main()
