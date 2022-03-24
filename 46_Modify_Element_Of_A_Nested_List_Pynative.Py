"""
https://pynative.com/python-exercises-with-solutions/
Exercise 9: Modify the element of a nested list inside the following list

Change the element 35 to 3500

Given:

list1 = [5, [10, 15, [20, 25, [30, 35   ], 40], 45], 50]

Expected Output: -

[5, [10, 15, [20, 25, [30, 3500], 40], 45], 50]

"""

list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]

list1[1][2][2][1] = 3500

print(list1)
