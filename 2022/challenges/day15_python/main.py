import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
from dataclasses import dataclass
from typing import List

try:
    K = 2000000
    N = M = 4000000
    FILE = sys.argv[1] 
except:
    K = 10
    N = 20
    M = 4000000
    FILE = 'test.in'

@dataclass(eq=True, frozen=True)
class Point:
    y: int
    x: int

@dataclass
class Sensor:
    p: Point
    radius: int

@dataclass
class Interval:
    l: int
    r: int

def read_data(filename: str):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data

def taxicab_distance(p1, p2):
    return abs(p1.y - p2.y) + abs(p1.x - p2.x)


# I just need to identify max width and then I just brute force, actually there might be another way
# I have a point of where sensor is located, its radius and y position of the target line
# I have y1, y2 and x2, x2 and r
# |y1 - y2| + |x1 - x2| = r
# |x1-x2| <= a
# -a <= x1 - x2 <= a 
# -a + x2 <= x1 <= a + x2 

# Idea or implemintation error?
# Idea:
#   math is off | Most likely
#   misunderstanding the problem statement | Unlikely

# Implemintation:
#   merge sort is off
#   data parsing is wrong

# store them as an intervals, then merge overlapping intervals, and then check if there are any beacons in those intervals and then we got the result
def calc(sensor, y) -> Interval:
    a = sensor.radius - abs(sensor.p.y - y)
    l, r = -a+sensor.p.x, a+sensor.p.x
    if l <= r:
        return Interval(l, r)
    return None 

def merge_intervals(I: List[Interval]) -> List[Interval]:
    I.sort(key=lambda x: x.l)
    ans = [I[0]]
    for i in range(1, len(I)):
        interval = I[i]
        if ans[-1].r >= interval.l:
            ans[-1].r = max(interval.r, ans[-1].r)
        else:
            ans.append(interval)
    return ans


def partA(data) -> int:
    I = []
    for i, sensor in enumerate(data):
        #print(f'{i+1}/{len(data)}')
        res = calc(sensor, K)
        if res:
            I.append(res)
    intervals = merge_intervals(I) 
    result = 0
    for interval in intervals:
        result += interval.r - interval.l
    return result 


def partB(data):
    for i in range(N+1):
        I = []
        for sensor in data:
            #print(f'{i+1}/{len(data)}')
            res = calc(sensor, i)
            if res:
                I.append(res)
        intervals = merge_intervals(I) 
        for j in range(1, len(intervals)):
            if intervals[j-1].r >= 0 and intervals[j].l - intervals[j-1].r == 2:
                return ((intervals[j-1].r + 1) * M) + i

def parse_data(data):
    global beacons
    sensors = []
    beacons = set() 
    for line in data:
        line = line.split()
        sy = int(line[3].split('=')[1][:-1])
        sx = int(line[2].split('=')[1][:-1])
        by = int(line[9].split('=')[1])
        bx = int(line[8].split('=')[1][:-1])
        loc = Point(sy, sx)
        bloc = Point(by, bx)
        distance = taxicab_distance(loc, bloc) 
        sensors.append(Sensor(loc, distance))
        beacons.add(bloc)
    return sensors 

data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
