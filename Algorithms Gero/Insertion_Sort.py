numbers = [34, 56, 12, 32, 54, 47, 8, 43]


def insertion_sort(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    sorted_nums = []
    for num in nums:
        for i in range(len(sorted_nums)):
            if num < sorted_nums[i]:
                sorted_nums.insert(i, num)
                break
        else:
            sorted_nums.append(num)

    return sorted_nums


print("insertion_sort(numbers): ", insertion_sort(numbers))
