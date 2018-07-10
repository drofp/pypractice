#!usr/bin/env python3

"""Example 5 from https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
==========================
- Randomly generate 2 lists of integers for testing.

- Print a list of all values in both input lists.
"""

import random

def main(testList1, testList2):
    print("common list:", list(x for x in testList1 if x in testList2))

if __name__ == "__main__":
    testList1 = [x for x in range(random.randint(-10, -1), random.randint(0, 10))]
    testList2 = [x for x in range(random.randint(-10, -1), random.randint(0, 10))]

    print("testList1:", testList1,
          "\ntestList2:", testList2)

    main(testList1, testList2)