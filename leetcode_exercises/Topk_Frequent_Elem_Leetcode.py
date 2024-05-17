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


def topK_frequent(nums: list, k: int) -> list[int]:
    count = {}

    freq = [[] for _ in range(len(nums) + 1)]

    for n in nums:
        count[n] = count.get(n, 0) + 1

    for n, c in count.items():
        freq[c].append(n)

    res = []

    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


nums = [3, 3, 3, 4, 4, 5, 7, 7, 7, 7]
k = 2

r = topK_frequent(nums, k)
print("r: ", r)
