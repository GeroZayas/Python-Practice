from typing import List

numbers = [19, 12, 20, 15, 22, 17, 18, 16, 29]


def quick_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = [x for x in nums[1:] if x < pivot]
    right = [x for x in nums[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


print("quick_sort(numbers): ", quick_sort(numbers))

"""
# Test Cases for quick_sort function

# Happy Path Tests
def test_quick_sort_happy_path():
    """
# Arrange
nums = [4, 2, 7, 1, 9]

# Act
sorted_nums = quick_sort(nums)

# Assert
assert sorted_nums == [1, 2, 4, 7, 9]


def test_quick_sort_empty_list():
    """
        # Arrange
        nums = []

        # Act
        sorted_nums = quick_sort(nums)

        # Assert
        assert sorted_nums == []

    def test_quick_sort_single_element():
    """
    # Arrange
    nums = [5]

    # Act
    sorted_nums = quick_sort(nums)

    # Assert
    assert sorted_nums == [5]


# Edge Cases
def test_quick_sort_duplicate_elements():
    """
        # Arrange
        nums = [3, 2, 1, 2, 3]

        # Act
        sorted_nums = quick_sort(nums)

        # Assert
        assert sorted_nums == [1, 2, 2, 3, 3]

    def test_quick_sort_already_sorted():
    """
    # Arrange
    nums = [1, 2, 3, 4, 5]

    # Act
    sorted_nums = quick_sort(nums)

    # Assert
