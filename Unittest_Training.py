import unittest


def square(x):
    # print(f"The square of {x} is:")
    return x**2


print(square(4))


class TestSquare(unittest.TestCase):
    def test_square_first(self):
        self.assertEqual(first=square(4), msg="TESTING MESSAGE", second=16)

    def test_square_second(self):
        self.assertEqual(first=square(8), msg="TESTING MESSAGE NUMBER 2", second=64)


if __name__ == "__main__":
    unittest.main()
