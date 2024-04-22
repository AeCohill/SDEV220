import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        result = sum([1, 2, 3])
        self.assertEqual(result, 6, "Should be 6")
        print("Test sum([1, 2, 3]) =", result)

    def test_sum_tuple(self):
        result = sum((1, 2, 2))
        self.assertEqual(result, 6, "Should be 6")
        print("Test sum((1, 2, 2)) =", result)

if __name__ == '__main__':
    unittest.main()