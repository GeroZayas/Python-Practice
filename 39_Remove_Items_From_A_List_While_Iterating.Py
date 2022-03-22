"""
Exercise 3: Remove items from a list while iterating
Description:

In this question, You need to remove items from a list while iterating but without creating a different copy of a list.

Remove numbers greater than 50
"""

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Before       ", number_list)

number_list = [x for x in number_list if x <= 50]

print("****************************")

print("After       ", number_list)
