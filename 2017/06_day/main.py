import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
import math
from dataclasses import dataclass

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'


def read_data(filename: str):
    with open(filename, 'r') as f:
        return list(map(int, f.read().strip().split()))


# save state,
# find largest one, calculate how many time we would wrap around for the current bank, and add that many number of blocks
# I need to identify how to get around circular array and record how many times I passed current index
# current_pos, length, val
def partA(data):
    s = set()
    n = len(data)
    step = 0
    while tuple(data) not in s:
        s.add(tuple(data))
        i, _ = max(enumerate(data), key=lambda x: x[1])
        val = data[i]
        data[i] = 0
        for j in range(i + 1, i + val + 1):
            data[(j) % n] += 1
        step += 1

    return step


def partB(data):
    s = set()
    n = len(data)
    step = 0
    while tuple(data) not in s:
        s.add(tuple(data))
        i, _ = max(enumerate(data), key=lambda x: x[1])
        val = data[i]
        data[i] = 0
        for j in range(i + 1, i + val + 1):
            data[(j) % n] += 1
        step += 1
    return step


def parse_data(data):
    return data


data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
