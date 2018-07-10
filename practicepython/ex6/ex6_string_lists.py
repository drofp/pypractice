#!usr/bin/env python3

"""Example 6 from https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
==========================
- Prompt user for a string

- Print whether user's string is a palindrome or not
"""

def main():
    maybePalindrome = input("Enter some string.\n" +
                             "--> ")

    for letterIdx in range(len(maybePalindrome)):
        if maybePalindrome[letterIdx] != maybePalindrome[len(maybePalindrome)-1-letterIdx]:
            print("It's NOT a palindrome!")
            return
    
    print("It's a palindrome!")

if __name__ == "__main__":
    main()
