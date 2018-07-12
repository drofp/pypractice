"""Exercise 11 from https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

- Removes duplicates from a list.
Uses a trick on list mutations mentioned in the comment sections of the solutions by Michele Pratusevich.
"""

someList = [x for x in range(11)]
someList.append(1)
someList.append(2)

someListWithoutDuplicates = []
[someListWithoutDuplicates.append(x) for x in someList if x not in someListWithoutDuplicates]

print("someList:                  {}\nsomeListWithoutDuplicates: {}".format(someList, someListWithoutDuplicates))
