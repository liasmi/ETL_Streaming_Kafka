
from GenericValidators.src.utils.RequiredField import hello

import unittest
 
# Define a test suite targeting specific functionality
class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    def test_that_riddle_is_solved(self):
        
        self.assertEqual(hello(),"")
 
 
if __name__ == '__main__':
    unittest.main()