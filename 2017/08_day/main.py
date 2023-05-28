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

ops = {
    '<': operator.lt,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
    '>=': operator.ge,
    '>': operator.gt,
    'inc': operator.add,
    'dec': operator.sub
}


def read_data(filename: str):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data


def partA(data):
    d = defaultdict(int)
    for line in data:
        line = line.split()
        root = line[0]
        operation = line[5]
        n, query = int(line[-1]), line[4]
        a = int(line[2])

        if ops[operation](d[query], n):
            d[root] = ops[line[1]](d[root], a)
    return max(d.values())


def partB(data):
    val = defaultdict(int)
    res = 0
    for line in data:
        line = line.split()
        root = line[0]
        operation = line[5]
        n, query = int(line[-1]), line[4]
        a = int(line[2])

        if ops[operation](val[query], n):
            val[root] = ops[line[1]](val[root], a)
        res = max(res, *val.values())

    return res


def parse_data(data):
    return data


data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
