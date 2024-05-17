# Three sum

"""
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

"""


def three_sum(nums: list) -> list:
    res = []
    # we sort the array in-place
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            three_sum = a + nums[l] + nums[r]
            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:  # we have found a three sum thats adds up to 0
                res.append([a, nums[l], nums[r]])
                # now we need to update our pointers, but only
                # the l one, because the conditions in the while
                # loop take care of updating the others
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1

    return res


nums = [-1, 0, 1, 2, -1, -4]


res = three_sum(nums=nums)  # [[-1,-1,2],[-1,0,1]]z

print("res: ", res)
