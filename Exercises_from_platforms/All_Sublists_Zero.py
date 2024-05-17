def print_all_sublists(nums):
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total == 0:
                print("Sublist", (nums[i : j + 1]))


if __name__ == "__main__":
    nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    print_all_sublists(nums)
