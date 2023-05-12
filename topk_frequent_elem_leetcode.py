# from typing import List

# '''
# Given an integer array nums and an integer k, 
# return the k most frequent elements. 
# You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# '''

# def topKFrequent(nums: List[int], k: int) -> List[int]:
#     numbers = {n:0 for n in set(nums)}
#     print(numbers)
#     for num in nums:
#         numbers[num]+= 1
        
#     freq = {}
#     for key, value in numbers.items():
#         if value in freq:
#             freq[value].append(key)
#         else:
#             freq[value] = [key]

#     result = []
#     for count in sorted(freq, reverse=True):
#         result.extend(freq[count])
#         if len(result) >= k:
#             break

#     return result # type: ignore

# nums = [1,1,1,1,1,1,2,2,3,3,3,3,3,3,3,3,3,3,3]
# k = 2

# r = topKFrequent(nums, k)

# print('r = topKFrequent(nums, k): ', r)

def topK_frequent(nums:list, k:int)->list[int]:
    
    
nums = [1,1,1,2,2,3,4,4,4,4,4,4]; k = 2

r = topK_frequent(nums, k)
print('r: ', r)
