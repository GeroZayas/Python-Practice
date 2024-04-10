import unittest


def generate_coordinates(x, y, z, n):
    return [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

class TestCoordinatesGeneration(unittest.TestCase):
    def test_generate_coordinates(self):
        expected_result = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
        self.assertEqual(generate_coordinates(1,1,1,2), expected_result)

        
if __name__ == "__main__":
    unittest.main()