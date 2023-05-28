import unittest
from main import read_data, second, first, count_magnitude

class TestingPart2(unittest.TestCase):
#    def test_example(self):
#        l = read_data('test2')
#        self.assertEqual(second(l), 3993)
#

# this test fail for some reason
    def test_addition_with_simplification(self):
        l = [
            [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]],
            [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
        ]
        self.assertEqual(first(l), count_magnitude([[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]))
