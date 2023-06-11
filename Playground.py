def quicksort(arr:list)->list:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)

from random import randint

numbers = [randint(1,20) for _ in range(10)]

print(numbers)

print(quicksort(numbers))
    