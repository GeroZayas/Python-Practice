from typing import List

# from random import randint

# numbers = [randint(1, 30) for _ in range(9)]
# print("numbers: ", numbers)

numbers = [19, 12, 20, 15, 22, 17, 18, 16, 29]


def quick_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = [x for x in nums[1:] if x < pivot]
    right = [x for x in nums[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


print("quick_sort(numbers): ", quick_sort(numbers))
