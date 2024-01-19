from typing import List

# from random import randint

# numbers = [randint(1, 30) for _ in range(9)]
# print("numbers: ", numbers)

numbers = [19, 12, 20, 15, 22, 17, 18, 16, 29]

def quicksort(numbers:list) -> list:
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    left = [e for e in numbers[1:] if e < pivot]
    right = [e for e in numbers[1:] if e >= pivot]
    return quicksort(left) + [pivot] + \
        quicksort(right)

print(quicksort(numbers))
    

