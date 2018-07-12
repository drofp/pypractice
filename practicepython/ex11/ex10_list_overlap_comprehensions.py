#!/usr/bin/env python3

"""Example 11 from https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
==========================
- Tell user if the positive integer they input is prime or not

Using "Optimized School Method" from: https://www.geeksforgeeks.org/primality-test-set-1-introduction-and-school-method/
"""

def isPrime(someNumber):

    # Corner cases
    if someNumber <= 1:
        return False
    if someNumber <= 3:
        return True

    if someNumber % 2 == 0 or someNumber % 3 == 0:
        return False

    i = 5
    while (i*i < someNumber):
        if someNumber % i == 0 or someNumber % (i + 2) == 0:
            return False
        i += 6

    return True

def main():
    
    # Assumes input is valid
    userNumber = int(input("Please enter a positive integer" +
                           "--> "))

    if isPrime(userNumber):
        print("Your number, {}, is prime!".format(userNumber))
    else:
        print("Your number, {}, is not prime!".format(userNumber))
        


if __name__ == "__main__":
    main()
