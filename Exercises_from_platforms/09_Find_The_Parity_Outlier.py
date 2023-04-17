"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
"""


def find_outlier(integers):
    outlier = int

    # To determine if we are dealing with odd or even nums:
    # We create a bool var
    nums_are_even = bool

    even_counter = 0
    odds_counter = 0

    # If there are more even nums in integers, then the outlier is odd, and viceversa
    for num in integers:
        if num % 2 == 0:
            even_counter += 1
        else:
            odds_counter += 1

    # Nums are even is True if there are more of those than of odd
    if even_counter > odds_counter:
        nums_are_even = True
    else:
        nums_are_even = False

    # We create a boolean var found_outlier and we set it to false, since we have to find it next
    found_outlier = False

    # We create a while loop to find the outlier, and one we find it found_outlier becomes true and breaks the while loop
    while found_outlier is False:
        if nums_are_even:
            for num in integers:
                if num % 2 != 0 or num % -2 != 0:
                    outlier = num
                    found_outlier = True
                    if found_outlier is True:
                        break
        else:
            for num in integers:
                if num % 2 == 0 or num % -2 == 0:
                    outlier = num
                    found_outlier = True
                    if found_outlier is True:
                        break
    return outlier


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))  # -> 11
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))  # -> 160
print(find_outlier([2, 4, 6, 8, 10, 3]))  # -> 3
print(find_outlier([-9213106, 5922141, -7860144, -2358100, -3308206, 1468196, -6470658,
      2704768, 3821070, 3372940, -7984648, 7824686, -95980, 795272, 4839724, 1505496, -4221688]))  # -> 5922141
