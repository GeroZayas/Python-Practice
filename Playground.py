numbers = [5, 4, 3, 7, 3, 2, 97, 68, 23, 56]
print(numbers)


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


sorted_numbers = quicksort(numbers)
print(sorted_numbers)


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return f'Element found at index {mid}'
        elif target < arr[mid]:
            right -= 1
        else:
            left += 1
    return 'Element not found in array'


print(binary_search(sorted_numbers, target=7))

