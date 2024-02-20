import unittest

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return f"Target found at index {mid}"
        elif target < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return f"Target not found"


target = 2
print(binary_search(my_list, target))


# =============== TEST ====================
class TestBinarySearch(unittest.TestCase):
    def test_find_target_3(self):
        self.assertEqual(binary_search(my_list, 3), "Target found at index 2")

    def test_find_target_3(self):
        self.assertEqual(binary_search(my_list, 9), "Target found at index 8")

    def test_find_target_3(self):
        self.assertEqual(binary_search(my_list, 10), "Target not found")


# =============== Run The Tests ====================
if __name__ == "__main__":
    unittest.main()
