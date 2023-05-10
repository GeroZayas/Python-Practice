

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [e for e in arr[1:] if e < pivot]
    right = [e for e in arr[1:] if e >= pivot]
    
    return quicksort(left) + [pivot] + quicksort(right)

