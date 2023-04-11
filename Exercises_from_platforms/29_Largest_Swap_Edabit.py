"""
Largest Swap

Write a function that takes a two-digit number and determines if it's the largest of two possible digit swaps.

To illustrate:

largest_swap(27) ➞ False

largest_swap(43) ➞ True

If 27 is our input, we should return False because swapping the digits gives us 72, and 72 > 27. On the other hand, swapping 43 gives us 34, and 43 > 34.

Examples
largest_swap(14) ➞ False

largest_swap(53) ➞ True

largest_swap(99) ➞ True

Notes
Numbers with two identical digits (third example) should yield True (you can't do better).

"""


def largest_swap(num: int) -> bool:
    swap_num = str(num)
    swap_num = int(swap_num[::-1])
    return True if num > swap_num or swap_num == num else False


print(largest_swap(99))  # True
print(largest_swap(14))  # False
