from random import choice

# numbers = [randint(1,30) for _ in range(1,20)]

numbers = [45, 32, 22, 1, 78, 20, 48]

print("This is numbers:\n", numbers, "\n\n")


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = []
    right = []

    for num in nums[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return quicksort(left) + [pivot] + quicksort(right)


print("This is numbers sorted:")
print(quicksort(numbers))

sorted_numbers = quicksort(numbers)

# IMPLEMENT BINARY SEARCH RECURSIVELY TO FIND A TARGET ELEMENT IN NUMBERS ARRAY


def binary_search(nums: list, left, right, target: int):
    if left > right:
        return f"Element {target} not found in array."

    mid = (left + right) // 2

    if target == nums[mid]:
        return f"Element {target} found at index {mid}"

    elif target < nums[mid]:
        return binary_search(nums, left, mid - 1, target)
    else:
        return binary_search(nums, mid + 1, right, target)


target = choice(sorted_numbers)

print(f"\n This is target {target}")

result = binary_search(sorted_numbers, 0, (len(sorted_numbers) - 1), target)

print()
print()

print(result)
