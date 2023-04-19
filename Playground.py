nums = [6,4,9,8,2,4,6,2,5,8,9]

print('This is nums => ', nums)

# --------------------------------------------------------
# QUICK SORT ALGO
# --------------------------------------------------------

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []

    for e in arr[1:]:
        if e < pivot:
            left.append(e)
        else:
            right.append(e)

    return quicksort(left) + [pivot] + quicksort(right)

sorted_arr = quicksort(nums)

print("This is sorted arr", sorted_arr)

# --------------------------------------------------------
# BINARY SEARCH
# --------------------------------------------------------

def binary_search(arr, left, right, target):
    if left > right:
        return -1
    mid = (left + right) // 2

    if target == arr[mid]:
        return f'Element {target} found at index {mid}'
    elif target > arr[mid]:
        return binary_search(arr, mid + 1, right, target)
    else:
        return binary_search(arr, left, mid - 1, target)

print(binary_search(sorted_arr, 0, len(sorted_arr)-1, 5))


