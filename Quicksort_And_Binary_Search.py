from random import choice

numbers  = [5,4,8,7,3,2]

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

# binary search to find random_num_from_arr

random_num_from_arr = choice(numbers)
print("Choice is", random_num_from_arr)

def binary_search(arr, left, right, target):
    if left > right:
        return "Element not found"

    mid = (left + right) // 2

    if target == arr[mid]:
        return f"Element {target} found at index {mid}"
    elif target < arr[mid]:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)

print(f"{binary_search(sorted_numbers, 0, len(sorted_numbers)-1, random_num_from_arr)}")

