arr = [-2, 45, 0, 11, -9,88,-97,-202,747]

print("This is arr => ",arr)

def quicksort(arr):
    size = len(arr)
    if size <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)
                
        
        
print('This is sorted arr => ', quicksort(arr))


