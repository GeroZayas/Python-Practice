def bs(nums:list, target:int):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return f"Element found at index {mid}"
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return f"Element {target} not found in array"

target = 56

numbers = [2,43,67,43,89,56,23,21,34]
sorted_nums = sorted(numbers)
print(sorted_nums)

print("Apply binary search:")
r = bs(sorted_nums, target)
print(r)