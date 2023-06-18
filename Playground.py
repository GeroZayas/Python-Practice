def quicksort(arr:int)->int:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)

from random import randint

numbers = [randint(1,100) for _ in range(10)]
print(f"This is numbers: {numbers}")
sorted_numbers = quicksort(numbers)
print(f"This is sorted numbers: {sorted_numbers}")
