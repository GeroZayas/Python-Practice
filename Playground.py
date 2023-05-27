numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("numbers: ", numbers)


def quicksort(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = [n for n in nums[1:] if n < pivot]
    right = [n for n in nums[1:] if n >= pivot]

    return quicksort(left) + [pivot] + quicksort(right)


sorted_nums = quicksort(numbers)
print("sorted_nums: ", sorted_nums)

target = 8


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return f"Element {target} found at index {mid}"
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return f"Element {target} not found"


print(binary_search(sorted_nums, target))
