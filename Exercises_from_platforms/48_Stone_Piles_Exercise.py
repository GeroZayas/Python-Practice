"""
https://www.w3resource.com/python-exercises/puzzles/index.php#EDITOR

4. We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile.

Input: 2

Output:
[2, 4]

Input: 10

Output:
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

Input: 3

Output:
[3, 5, 7]

Input: 17

Output:
[17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
"""

# TODO check if input is even or odd
# If even, all piles must have an even number of stones.

the_inputs = [2, 10, 3, 17]


# TODO print a list with the piles


def print_piles(the_amount):
    pile = []
    for x in range(the_amount):
        pile.append(the_amount)
        the_amount += 2
    return pile


# IMPORTANT: Notice tha t when we call the function in map we don't use the parentheses ()
all_together = list(map(print_piles, the_inputs))

for element in all_together:
    print(" *** ", element)
