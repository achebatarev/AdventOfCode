import unittest
from main import read_data, beacon_overlapping,Pos

class Test(unittest.TestCase):
    def test_beacon_overlapping(self):
        l = read_data('test1')
#        a = [
#            686,422,578
#            605,423,415
#            515,917,-361
#            -336,658,858
#            -476,619,847
#            -460,603,-452
#            729,430,532
#            -322,571,750
#            -355,545,-477
#            413,935,-424
#            -391,539,-444
#            553,889,-390
#            ]
        self.assertEqual(beacon_overlapping(l[0], l[1], 3), Pos(5,2,0))




