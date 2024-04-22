import unittest
# Imports sum() from the my_sum package you created
from my_sum import sum

#Defines a new test case class called 
#TestSum, which inherits from unittest.TestCase
class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
   
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
#Defines a test method, .test_list_int(), to test a list of integers. The method .test_list_int() will:

#Declare a variable data with a list of numbers (1, 2, 3)
#Assign the result of my_sum.sum(data) to a result variable
# of result equals 6 by using the .assertEqual() method on the unittest.TestCase class
#Defines a command-line entry point, which runs the unittest test-runner .main()