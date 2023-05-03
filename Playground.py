from random import randint, choice

numbers = [randint(1,30) for _ in range(9)]

print('numbers: ', numbers)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    
    return quicksort(left) + [pivot] + quicksort(right)

sorted_numbers = quicksort(numbers)

print('sorted_numbers : ', sorted_numbers )

##########################################################
print("-" * 60)
##########################################################

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        
        if target == arr[mid]:
            return f"Element {target} found at index {mid}"
        elif target < arr[mid]:
            return binary_search(arr[:mid-1], target)
        else:
            return binary_search(arr[mid+1:], target)
        
    return "Element not found in array"

target = choice(sorted_numbers)
print(target)

r = binary_search(sorted_numbers, target)

print(r)






