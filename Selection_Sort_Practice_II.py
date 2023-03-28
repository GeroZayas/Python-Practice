# selection sort practice

from random import randint

numbers = [randint(1,8) for _ in range(4)]

print(numbers)
print(len(numbers))

def selection_sort(arr:list)->None:
    if len(arr) <= 1:
        return arr
    for i in range(len(arr) - 1):
        smallest_num_index = i
        for j in range(smallest_num_index + 1, len(arr)):
            if arr[j] < arr[smallest_num_index]:
                smallest_num_index = j
        arr[i], arr[smallest_num_index] = arr[smallest_num_index], arr[i]
        
selection_sort(numbers)

print("Sorted numbers:", numbers)

