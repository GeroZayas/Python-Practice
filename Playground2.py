from random import randint

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [e for e in arr[1:] if e < pivot]
    right = [e for e in arr[1:] if e >= pivot]
    
    return quicksort(left) + [pivot] + quicksort(right)

numbers = [randint(1,20) for _ in range(10)]
print('numbers: ', numbers)

# ----------------------------------------------------------------

print("-" * 60) # CONSOLE SEP

res = quicksort(numbers)
print('res: ', res)


# ----------------------------------------------------------------

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
    return "Element not found in array"

