arr = [-2, 45, 0, 11, -9,88,-97,-202,747]

print("This is arr => ",arr)

def selection_sort(arr):
    size = len(arr)
    if size <= 1:
        return arr
    
    min_idx = 0

    for i in range(size):
        min_idx = i
        for j in range(i+1, size):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

selection_sort(arr)

print('This is sorted arr => ', arr)


