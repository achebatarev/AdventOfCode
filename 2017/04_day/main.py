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
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip().split())
    return data


def partA(data) -> int:
    return sum(len(set(e)) == len(e) for e in data)


def partB(data) -> int:
    l = [[''.join(sorted(c)) for c in a] for a in data]
    return sum(len(set(e)) == len(e) for e in l)


def parse_data(data):
    return data


data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
