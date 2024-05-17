# from random import randint

# my_list_of_nums = [randint(1,30) for _ in range(10)]

numbers = [15, 27, 23, 4, 8, 23, 9, 21, 26, 25]

print(numbers)


def quicksort(nums: list):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = [x for x in nums[1:] if x < pivot]
    right = [x for x in nums[1:] if x >= pivot]

    return quicksort(left) + [pivot] + quicksort(right)


sorted_numbers = quicksort(numbers)
print(sorted_numbers)

# Binary Search
target = 23
print(f"Target = {target}")


def binarysearch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return f"Target found at index {mid}"
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return f"Target {target} not found in array"


r = binarysearch(sorted_numbers, target)
print(r)
