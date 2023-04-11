numbers = [5,6,4,3,7,2,1]

# GOAL Selection Sort the array

def selection_sort(nums:list) -> list:
    # base case
    if len(nums) <= 1:
        return nums

    for index in range(len(nums)-1):
        current_min_index = index
        for j_index in range(current_min_index + 1, len(nums)):
            if nums[j_index] < nums[current_min_index]:
                current_min_index = j_index
        nums[index], nums[current_min_index] = nums[current_min_index], nums[index] # swap

print("Numbers:", numbers)        

selection_sort(numbers)

print("Numbers sorted:", numbers)

