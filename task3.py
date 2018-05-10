"""
===================   TASK 3  ====================
* Name: Recursive Sum
*
* Write a recursive function that will sum given
* list of integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def getSum(iterable):
    if not iterable:
        return 0  # End of recursion
    else:
        return iterable[0] + getSum(iterable[1:])  # Recursion step