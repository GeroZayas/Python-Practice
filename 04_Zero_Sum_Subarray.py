from typing import List

int_array = [4, 6, -4, -2, 1]


def hasZeroSumSubarray(nums: List[int]) -> bool:
    the_sum = set()
    the_sum.add(0)
    total = 0
    for n in nums:
        total += n
        if total in the_sum:
            return True
    return False


print(hasZeroSumSubarray(int_array))
