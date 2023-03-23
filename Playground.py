from random import randint

# TODO Implement 1 - Insertion Sort Algo
# TODO Implement 2 - QuickSort Algo
# TODO Implement 3 - MergeSort Algo

# Arr of random ints:

rand_arr = [randint(1, 101) for _ in range(9)]
print("rand_arr: ", rand_arr)


# insertion sort


def insertion_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    ord_arr = []

    for num in arr:
        for i in range(len(ord_arr)):
            if num < ord_arr[i]:
                ord_arr.insert(i, num)
                break
        else:
            ord_arr.append(num)
    return ord_arr


print("insertion sort:", insertion_sort(rand_arr))

# quicksort algo


def quicksort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []

    for num in arr[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return quicksort(left) + [pivot] + quicksort(right)


print("Quicksort:", quicksort(rand_arr))


# merge sort


def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_h = arr[:mid]
    right_h = arr[mid:]

    left_h = merge_sort(left_h)
    right_h = merge_sort(right_h)

    return merge(left_h, right_h)


def merge(left: list, right: list) -> list:
    ord_arr = []

    l_idx = r_idx = 0

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            ord_arr.append(left[l_idx])
            l_idx += 1
        else:
            ord_arr.append(right[r_idx])
            r_idx += 1

    ord_arr += left[l_idx:]
    ord_arr += right[r_idx:]

    return ord_arr


print("merge sort:", merge_sort(rand_arr))
