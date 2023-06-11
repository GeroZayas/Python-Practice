def quicksort(arr:list)->list:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]