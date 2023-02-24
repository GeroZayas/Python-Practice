"""
Exercise 4: Reverse Dictionary mapping

https://pynative.com/python-exercises-with-solutions/

Given:

ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}

Expected Output:

{65: 'A', 66: 'B', 67: 'C', 68: 'D'}
"""
ascii_dict = {"A": 65, "B": 66, "C": 67, "D": 68}
print(ascii_dict)  # {'A': 65, 'B': 66, 'C': 67, 'D': 68}

reverse_map = {}

for k, v in ascii_dict.items():
    reverse_map[v] = k

print(reverse_map)  # {65: 'A', 66: 'B', 67: 'C', 68: 'D'}

# another way, with a dict comprehension

second_rev_map = {v: k for k, v in ascii_dict.items()}
print(second_rev_map)  # {65: 'A', 66: 'B', 67: 'C', 68: 'D'}
