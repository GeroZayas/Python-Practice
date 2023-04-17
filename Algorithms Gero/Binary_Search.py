# from random import randint

# # Generate an arr of nums
# numbers = [randint(1, 101) for _ in range(20)]
# print("numbers: ", numbers)

numbers = [12, 93, 67, 68, 53, 7, 25, 40, 4, 60, 65, 35, 80, 58, 30, 18, 11, 76, 48, 63]


# SORT the numbers using quick sort
def quick_sort(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    pivot, left, right = nums[0], [], []

    for num in nums[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return quick_sort(left) + [pivot] + quick_sort(right)


sorted_numbers = quick_sort(numbers)
print("sorted_numbers: ", sorted_numbers)

# IMPLEMENT Binary Search (recursively) to find a target num


def binary_search(nums, left, right, target):
    if left > right:
        return f"Element [{target}] not found in array"

    mid = (left + right) // 2

    if target == nums[mid]:
        return f"Element [{target}] found at index {mid}"
    elif target < nums[mid]:
        return binary_search(nums, left, mid - 1, target)
    else:
        return binary_search(nums, mid + 1, right, target)


target, left, right = 80, 0, len(sorted_numbers) - 1

r = binary_search(nums=sorted_numbers, left=left, right=right, target=target)

print(f"binary_search: ", r)
