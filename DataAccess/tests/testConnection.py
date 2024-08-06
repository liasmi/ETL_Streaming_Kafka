
from Dags.src.utils.kafka_stream import hello

import unittest
 
# Define a test suite targeting specific functionality
class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    def test_that_riddle_is_solved(self):
        
        self.assertEqual(hello(),"")
 
 
if __name__ == '__main__':
    unittest.main()