numbers = [4,5,3,2,1,7,6]
print("This is numbers", numbers)

# quick sort | merge sort | insertion sort | selection sort

# Sort the numbers array using selection sort
def selection_sort(nums):
    if len(nums) <= 1:
        return nums
        
    min_index = 0

    for i in range(min_index + 1, len(nums)):
        if nums[i] < nums[min_index]:
            min_index = i
    nums[min_index], nums[0] = nums[0], nums[min_index]

    return [nums[0]] + selection_sort(nums[1:])

# binary search

sorted_nums = selection_sort(numbers)

print("""
this is sorted_nums
""")
print(sorted_nums)

# Binary search

target = 5

def binary_search(arr, left, right, target):
    if left > right:
        return "Element not found"

    mid = (left + right) // 2

    if  target == arr[mid]:
        return f"Element {target} found at index {mid}"
    elif target < arr[mid]:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)

result = binary_search(sorted_nums, 0, len(sorted_nums) - 1, target)

print(
    f"""
    This is the result:

    {result}

    """
)
