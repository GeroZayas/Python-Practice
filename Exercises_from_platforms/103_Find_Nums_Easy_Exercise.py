# Python Programming Puzzles [100 exercises with solution]
# https://www.w3resource.com/python-exercises/puzzles/index.php

"""
1. Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Go to the editor
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
True
"""

the_input = [19, 19, 15, 5, 3, 5, 5, 2]


def find_nums(an_input: list) -> bool:
    counter_19 = 0
    counter_5 = 0

    for n in the_input:
        if n == 19:
            counter_19 += 1
        if n == 5:
            counter_5 += 1

    if counter_19 == 2 and counter_5 >= 3:
        return True

    return False


print(find_nums(the_input))


def find_nums_count(an_input: list) -> bool:
    return an_input.count(19) == 2 and an_input.count(5) >= 3


print(find_nums_count(the_input))
