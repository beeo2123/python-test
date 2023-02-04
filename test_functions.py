import unittest
import sys
sys.path.append('../AtlasCopcoSoftwareTesterTest')
from various_methods import VariousMethods






class FindMax(unittest.TestCase):
    def setup(self):
        self.methods = VariousMethods()

    def test_something(self):
        print('sssss', VariousMethods.FindMax([1,2]))
        print('1231231',self.methods.FindMax([1,2,3]))
        self.assertEqual(self.methods.FindMax([1,2,3,4,5]), 5)  # add assertion here


if __name__ == '__main__':
    unittest.main()
