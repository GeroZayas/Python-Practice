numbers= [7,6,5,4,3,8,2,1]
print(numbers)

# insertion sort
def insertion_sort(nums):
    if len(nums)<=1:
        return nums
    sorted_nums = []
    for num in nums:
        for i in range(len(sorted_nums)):
            if num < sorted_nums[i]:
                sorted_nums.insert(i, num)
                break
        else:
            sorted_nums.append(num)

    return sorted_nums

result = insertion_sort(numbers)

print(result)

# SELECTION SORT (in place)
def selection_sort(nums):
    if len(nums) <= 1:
        return nums

    for i in range(len(nums) - 1):
        index_min = i
        for j in range(index_min + 1, len(nums)):
            if nums[j] < nums[index_min]:
                index_min = j
            nums[i], nums[index_min] = \
            nums[index_min], nums[i]

selection_sort(numbers)

print("Selection sorted numbers: ", numbers)

# merge sort
# quick sort

# binary search
 
