import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
import math
from dataclasses import dataclass
import operator
import functools
import re

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'


def read_data(filename: str):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data


def got_caught(data, start):
    finish = max(data)
    for i in range(finish + 1):
        time = start + start
        if i in data and time % ((data[i] - 1) * 2) == 0:
            return True
    return False


def partA(data):
    finish = max(data)
    ans = 0
    for i in range(finish + 1):
        if i in data and (i % ((data[i] - 1) * 2)) == 0:
            ans += i * data[i]
    return ans


# tachnically I just need to find the offset where I am not d
# If I collect all of the numbers, and find what
# if depth + initial
def partB(data):
    i = 0
    for depth, rang in data.items():
        circle = (rang - 1) * 2

        print(depth, circle, circle - depth)
    while True:
        if not got_caught(data, i):
            return i
        i += 1


def parse_data(data):
    d = {}
    for line in data:
        a = re.findall(r'\d+', line)
        d[int(a[0])] = int(a[1])
    return d


data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
