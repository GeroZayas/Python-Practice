def longest_consecutive_seq(nums: list[int]) -> int:
    longest = 0

    nums_set = set(nums)

    for n in nums:
        if (n - 1) not in nums_set:
            length = 0
            while (n + length) in nums_set:
                length += 1
            print(n, length)
            longest = max(length, longest)
    return longest


# nums = [1,2,3,4,100, 200]
nums = [3, 4, 2, 1, 0, 67, 69, 70, 71, 72, 73, 68, 75, 43]

res = longest_consecutive_seq(nums)

print(res)
