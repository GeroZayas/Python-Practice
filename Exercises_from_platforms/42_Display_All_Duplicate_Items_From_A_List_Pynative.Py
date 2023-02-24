"""
https://pynative.com/python-exercises-with-solutions/
Exercise 5: Display all duplicate items from a list

Given:

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

Expected Output: -

[20, 60, 30]
"""

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

duplicates = []

# We make use of method list.count()
for element in sample_list:
    if sample_list.count(element) == 2:
        if element not in duplicates:
            duplicates.append(element)

print(duplicates)
