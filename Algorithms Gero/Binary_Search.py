# from random import randint

# # Generate an arr of nums
# numbers = [randint(1, 101) for _ in range(20)]
# print("numbers: ", numbers)

numbers = [12, 93, 67, 68, 53, 7, 25, 40, 4, 60, 65, 35, 80, 58, 30, 18, 11, 76, 48, 63]


# SORT the numbers using quick sort
def quick_sort(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = [x for x in nums[1:] if x < pivot]
    right = [x for x in nums[1:] if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


sorted_numbers = quick_sort(numbers)
print("sorted_numbers: ", sorted_numbers)

# IMPLEMENT Binary Search (recursively) to find a target num


def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return f"Element {target} found at index {mid}"
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return f"Element {target} not found in array"


target = 68

r = binary_search(nums=sorted_numbers, target=target)

print("binary_search: ", r)

