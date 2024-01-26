# selection sort practice

from random import randint

numbers = [randint(1,1000) for _ in range(10)]

print(numbers)
print("This is length of numbers =>", len(numbers))

def selection_sort(arr:list[int])->None:
    if len(arr) <= 1:
        return arr
    for i in range(len(arr)-1):
        smallest_elem_idx = i
        for j in range(smallest_elem_idx + 1, len(arr)):
            if arr[j] < arr[smallest_elem_idx]:
                smallest_elem_idx = j
        arr[i], arr[smallest_elem_idx] \
        = arr[smallest_elem_idx], arr[i]



selection_sort(numbers)

print("Sorted numbers:", numbers)





