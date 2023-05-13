from random import randint, choice
from typing import List

numbers = [randint(1,100) for _ in range(10)]

print('numbers: ', numbers)

# ----------------------------------------------------------------

def quicksort(arr:List[int])-> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    
    return quicksort(left) + [pivot] + quicksort(right)

sorted_nums = quicksort(numbers)

print('sorted_nums : ', sorted_nums )

# ----------------------------------------------------------------

def binary_search(arr: List[int], target:int):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return f"Element {target} found at index {mid}"
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return "Element not found in array"

target = choice(sorted_nums)
print('target: ', target)

res = binary_search(sorted_nums, target)
print('binary_search: ', res)
