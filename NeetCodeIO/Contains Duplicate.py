from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
nums_2 = [4, 5, 6, 7, 8, 9]

solution = Solution()
print(solution.containsDuplicate(nums))  # Output: True
print(solution.containsDuplicate(nums_2))  # Output: False
