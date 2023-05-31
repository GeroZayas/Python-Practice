from random import randint as ri

numbers = [ri(1,1000000) for _ in range(100)]
print('numbers: ', numbers)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    
    return quicksort(left) + [pivot] + quicksort(right)

res = quicksort(numbers)

print("-" * 90)
print("-" * 90)
print("-" * 90)

print('res: ', res)

