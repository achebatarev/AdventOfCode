import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
import math
from dataclasses import dataclass
import operator

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'

steps = {
    'nw': (1, -1),
    'ne': (1, 1),
    'sw': (-1, -1),
    'se': (-1, 1),
    'n': (2, 0),
    's': (-2, 0),
}


@dataclass
class Point:
    y: int
    x: int


def read_data(filename: str):
    with open(filename, 'r') as f:
        return f.read().strip()


def calc_distance(pos):
    if abs(pos.y) > abs(pos.x):
        return (abs(pos.y) // 2) + abs(pos.x)
    return abs(pos.x)


# change my x, y and getting Chebushov distance is good enough?
# hex grid geometry
# I can travel diagonally and I can travel vertically
# I only need to travel vertically, when the diff between x and y is != 0
# My current formula assumes that moving vertically is always beneficial, which it is not always so
# moving vertically is only beneficial when y > x
def partA(data):
    pos = Point(0, 0)
    for step in data:
        y, x = steps[step]
        pos.y += y
        pos.x += x
    return calc_distance(pos)


def partB(data):
    res = 0
    pos = Point(0, 0)
    for step in data:
        y, x = steps[step]
        pos.y += y
        pos.x += x
        res = max(res, calc_distance(pos))
    return res


def parse_data(data):
    return data.split(',')


if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(partA(parsed_data))
    print(partB(parsed_data))
