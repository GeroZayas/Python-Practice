"""
First Factorial
Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and 18 and the input will always be an integer.
Examples
Input: 4
Output: 24
Input: 8
Output: 40320
"""


def FirstFactorial(num):
    final = 1
    while num > 0:
        final += final * (num - 1)
        num = num - 1
    return final


print(format(FirstFactorial(4), "_d"))
print(format(FirstFactorial(8), "_d"))
print(format(FirstFactorial(16), "_d"))
