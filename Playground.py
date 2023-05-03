from random import randint

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