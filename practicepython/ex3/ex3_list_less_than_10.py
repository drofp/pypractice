#!usr/bin/env python3

"""Example 3 from https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
==========================
GIVEN: A list of numbers

- Ask user for a number.

- In one line, print a new list that contains all elements from the original list that are less than 
the input number
"""

def main(someList):
    chosenVal = int(input("Enter a number.\n" +
                          "All values in a given list larger than or equal to this number will be filtered out.\n" +
                          "--> "))

    print("The given list is:", someList)

    print("The new list is:  ", list(val for val in someList if val < chosenVal))

if __name__ == "__main__":
    testList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    main(testList)
