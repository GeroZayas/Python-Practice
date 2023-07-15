def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

numbers = [5, 3, 2, 1, 4]

res = quicksort(numbers)
print(f"==>> res: {res}")

def binary_search(arr, target):
    if len(arr) == 0:
        return -1
    mid = len(arr) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr[mid + 1:], target)
    else:
        return binary_search(arr[:mid], target)

res = binary_search(res, 3)
print(f"==>> res: {res}")

