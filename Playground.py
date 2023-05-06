from random import choice

numbers = [7,3,2,54,8,24,85,23]
print('numbers: ', numbers)

# Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    
    return quicksort(left) + [pivot] + quicksort(right)

sorted_numbers = quicksort(numbers)
print('sorted_numbers: ', sorted_numbers)


# Binary Search
def binary_search(arr, target):
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
    return "Element not found in arr" 

target = choice(sorted_numbers)
print('target : ', target )

r = binary_search(sorted_numbers, target)
print('r = binary_search: ', r)