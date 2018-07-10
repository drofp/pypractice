#!usr/bin/env python3

"""Example 7 from https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
==========================
GIVEN: A list of integers

- In one line, print another list that contains only the even integers from the given list
"""

def main(givenList):
    print(list(x for x in givenList if x % 2 ==0))

if __name__ == "__main__":
    testList = [x for x in range(15)]
    print("The test list is:", testList)

    main(testList)

