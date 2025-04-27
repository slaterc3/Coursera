import unittest

from mymodule import square, double, add 

class TestSquare(unittest.TestCase):
    def test1(self): 
        # Check that calling 'square(2)' returns 4.
        # This tests if the function correctly computes the square of 2.
        self.assertEqual(square(2), 4) # test when 2 is given as input the output is 4.
        # Check that calling 'square(3.0)' returns 9.0.
        # This tests if the function correctly computes the square of 3.0, verifying that it handles float inputs.
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.
        # Check that calling 'square(-3)' does not return -9.
        # This tests that the function's output is not -9, verifying that the square of -3 should be 9.
        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.
        

class TestDouble(unittest.TestCase):
    def test1(self): 
        # Check that calling 'double(2)' returns 4.
        # This tests if the function correctly computes double of 2.
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.
        # Check that calling 'double(-3.1)' returns -6.2.
        # This tests if the function correctly computes double of -3.1, verifying that it handles negative float inputs.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.
        # Check that calling 'double(0)' returns 0.
        # This tests if the function correctly computes double of 0, verifying that the function works for edge cases.
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.
        
class TestAdd(unittest.TestCase):
    def test1(self):
        self.assertEqual(add(2, 4), 6)
        
        self.assertEqual(add(0, 0), 0)
        
        self.assertEqual(add('hello', 'world'), 'helloworld')
    
# if __name__ == "__main__":
unittest.main()