from typing import List, Tuple

def findPair(nums: List[int], target: int)-> Tuple[int]:
    for i, n in enumerate(nums):
        if target - n in nums and nums[]target - n:
            return (n, target - n)
    return ()

nums = [5, 2, 6, 8, 1, 9] 
target = 12


r = findPair(nums, target)
print(r)
