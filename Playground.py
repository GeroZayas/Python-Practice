numbers = [7, 6, 5, 4, 3, 2, 1]

print("numbers: ", numbers)


# Merge Sort Algo
def merge_sort(arr: list):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    L = arr[:mid]
    R = arr[mid:]

    L = merge_sort(L)
    R = merge_sort(R)

    return merge(L, R)


def merge(left, right):
    sorted_arr = []
    # i -> left index
    # j -> right index
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr += left[i:]
    sorted_arr += right[j:]

    return sorted_arr


print("merge_sort: ", merge_sort(numbers))


# Insertion Sort Algo
def insertion_sort(arr):
    sorted_arr = []
