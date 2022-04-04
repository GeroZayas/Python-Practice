"""
+1 Array

Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

the array can't be empty
only non-negative, single digit integers are allowed
Return nil (or your language's equivalent) for invalid inputs.

Examples
For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]

"""


def up_array(arr):
    my_str = ""
    if arr != [] and all(i >= 0 for i in arr):
        for n in arr:
            my_str += str(n)
        my_int = int(my_str) + 1
        final_arr = [int(x) for x in str(my_int)]
        return final_arr
    return None


print(up_array([2, 3, 9]))
