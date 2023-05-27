def findPair(nums, target):
    nums.sort()
    low, high = 0, len(nums) - 1

    while low < high:
        if nums[low] + nums[high] == target:
            return f"Pair found ({nums[low]}, {nums[high]})"
        elif nums[low] + nums[high] < target:
            low += 1
        else:
            high -= 1

    return "Pair not found"


nums = [8, 7, 2, 5, 3, 1] # 1,2,3,5,7,8
target = 10
 
r = findPair(nums, target)

print(r)