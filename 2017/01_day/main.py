import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'


def read_data(filename: str):
    with open(filename, 'r') as f:
        return f.read().strip()


def partA(data):
    res = 0
    n = len(data)
    for i in range(len(data)):
        if data[i] == data[(i + 1) % n]:
            res += int(data[i])
    return res


def partB(data):
    res = 0
    n = len(data)
    m = n // 2
    for i in range(len(data)):
        if data[i] == data[(i + m) % n]:
            res += int(data[i])
    return res


def parse_data(data):
    return data


data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
