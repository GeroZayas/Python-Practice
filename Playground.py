
def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (nums[i], nums[j])
    return ()

arr = [8, 7, 2, 5, 3, 1]
target = 10

r = findPairs(arr, target)
print(r)


arr = [5, 2, 6, 8, 1, 9]
target = 12

r = findPairs(arr, target)
print(r)


arr = [1,1,1,1]
target = 2

r = findPairs(arr, target)
print(r)








