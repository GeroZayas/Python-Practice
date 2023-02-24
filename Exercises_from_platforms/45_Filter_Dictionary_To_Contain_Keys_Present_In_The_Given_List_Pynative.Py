"""
Exercise 6: Filter dictionary to contain keys present in the given list

https://pynative.com/python-exercises-with-solutions/

Given:

# Dictionary
d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}

# Filter dict using following keys
l1 = ['A', 'C', 'F']

Expected Output: -

new dict {'A': 65, 'C': 67, 'F': 70}
"""

# Dictionary
d1 = {"A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70}

# Filter dict using following keys
l1 = ["A", "C", "F"]

new_dict = {}

for k, v in d1.items():
    if k in l1:
        new_dict[k] = v

print(new_dict)  # {'A': 65, 'C': 67, 'F': 70}
