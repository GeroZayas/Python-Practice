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


