"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""

#  ---------------- GERO'S SOLUTION ------------------------
def move_zeros(array):
    """
    Takes an array and moves all of the zeros to the end, preserving the order of the other elements.

    >>> move_zeros([1, 0, 1, 2, 0, 1, 3])
    [1, 1, 2, 1, 3, 0, 0]
    >>> move_zeros([0, 1, 2, 3])
    [1, 2, 3, 0]
    >>> move_zeros([0, 0, 1, 0, 3, 0, 1])
    [1, 1, 3, 1, 0, 0, 0]
    """
    # create array of zeros, to add them later to final array
    zeros = []
    # find zeros in input array and add them to our zeros array
    for i in array:
        if i == 0:
            zeros.append(i)
    # declare final_array to be returned
    # fill it with numbers from input array if not 0
    final_array = [x for x in array if x != 0]
    # return both arrays with zeros at end
    return final_array + zeros


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))

print("-----------------------------")

# ----------------- CODE WARS SOLUTION ------------------------
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i != 0]
    return l + [0] * (len(arr) - len(l))


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
