import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
import math
from dataclasses import dataclass
import operator
import functools

try:
    FILE = sys.argv[1]
    k = 256
except:
    k = 5
    FILE = 'test.in'


def read_data(filename: str):
    with open(filename, 'r') as f:
        return f.read().strip()


def reverse(arr, l, r):
    n = len(arr)
    while l < r:
        arr[l % n], arr[r % n] = arr[r % n], arr[l % n]
        l += 1
        r -= 1


def round(arr, i, skip, lenghts):
    for length in lenghts:
        reverse(arr, i, (i + length) - 1)
        i = (i + length + skip) % len(arr)
        skip += 1
    return i, skip


def partA(data):
    data = list(map(int, data.split(',')))
    arr = list(range(k))
    round(arr, 0, 0, data)
    return arr[0] * arr[1]


# 64 rounds, same length sequence, current_position and skip preserved
def partB(data):
    codes = list(map(ord, data))
    codes += [17, 31, 73, 47, 23]
    n = 256
    arr = list(range(n))
    i, skip = 0, 0
    for _ in range(64):
        i, skip = round(arr, i, skip, codes)
    dense_hash = []
    for i in range(0, n, 16):
        dense_hash.append(functools.reduce(operator.xor, arr[i:i + 16]))
    return ''.join([hex(h)[2:] for h in dense_hash])


def parse_data(data):
    return data


data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
