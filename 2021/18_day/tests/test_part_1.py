import unittest

from main import count_magnitude, explode, split, addition, first, read_data

class MyTest(unittest.TestCase):
    def test_counting_magnitutde(self):
        self.assertEqual(count_magnitude([[1,2],[[3,4],5]]), 143)
        self.assertEqual(count_magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]]), 1384)
        self.assertEqual(count_magnitude([[[[1,1],[2,2]],[3,3]],[4,4]]), 445)
        self.assertEqual(count_magnitude([[[[3,0],[5,3]],[4,4]],[5,5]]), 791)
        self.assertEqual(count_magnitude([[[[5,0],[7,4]],[5,5]],[6,6]]), 1137)
        self.assertEqual(count_magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]), 3488)

    def test_explode(self):
        self.assertListEqual(explode([[[[[9,8],1],2],3],4]), [[[[0,9],2],3],4])
        self.assertListEqual(explode([7,[6,[5,[4,[3,2]]]]]), [7,[6,[5,[7,0]]]])
        self.assertListEqual(explode([[6,[5,[4,[3,2]]]],1]), [[6,[5,[7,0]]],3])
        self.assertListEqual(explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]), [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
        self.assertListEqual(explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]), [[3,[2,[8,0]]],[9,[5,[7,0]]]])
        self.assertListEqual(explode([[[[0,7],4],[7,[[8,4],9]]],[1,1]]), [[[[0,7],4],[15,[0,13]]],[1,1]])

    def test_split(self):
        self.assertListEqual(split([[[[0,7],4],[[7,8],[0,13]]],[1,1]])[0], [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]])

    def test_addition(self):
        self.assertListEqual(addition([1, 2],[[3, 4], 5]), [[1,2],[[3,4],5]])

    def test_addition_with_simplification(self):
        l = [
            [[[[4,3],4],4],[7,[[8,4],9]]],
            [1,1]
        ]
        self.assertEqual(first(l), count_magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]]))

    def test_test2(self):
        l = read_data('test2') 
        self.assertEqual(first(l),4140) 

    def test_test1(self):
        l = read_data('test1') 
        self.assertEqual(first(l),count_magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])) 


