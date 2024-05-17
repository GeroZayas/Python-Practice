"""
Given a 2D ( nested ) list ( array, vector,...) of size m * n,
your task is to find the sum of the minimum values in each row.

For Example:

[ [ 1, 2, 3, 4, 5 ]        #  minimum value of row is 1
, [ 5, 6, 7, 8, 9 ]        #  minimum value of row is 5
, [ 20, 21, 34, 56, 100 ]  #  minimum value of row is 20
]

So the function should return 26 because
the sum of the minimums is 1 + 5 + 20 = 26.

Note: You will always be given a non-empty list containing positive values.
"""


def sum_of_minimums(numbers: list) -> int:
    the_sum = 0
    for lst in numbers:
        min_value = min(lst)
        the_sum += min_value
    return the_sum


print(sum_of_minimums([[7, 9, 8, 6, 2], [6, 3, 5, 4, 3], [5, 8, 7, 4, 5]]))  # 9
