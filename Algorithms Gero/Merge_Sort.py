# from random import randint

# numbers = [randint(1, 30) for _ in range(9)]
# print("numbers: ", numbers)

numbers = [19, 12, 20, 15, 22, 17, 18, 16, 29]
names = ["Gero", "Mar", "Elisa"]
last_names = ["Gero", "Mar", "Elisa"]


def merge_sort(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_half = nums[:mid]
    right_half = nums[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    sorted_nums = []

    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_nums.append(left[left_index])
            left_index += 1
        else:
            sorted_nums.append(right[right_index])
            right_index += 1
    sorted_nums += left[left_index:]
    sorted_nums += right[right_index:]

    return sorted_nums


print("merge_sort(numbers): ", merge_sort(numbers))
