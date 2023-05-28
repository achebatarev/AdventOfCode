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


def dfs(graph, node, visited):
    if node in visited:
        return 0
    ans = 1
    visited.add(node)
    for child in graph[node]:
        ans += dfs(graph, child, visited)
    return ans


def partA(data):
    return dfs(data, '0', set())


def partB(data):
    ans = 0
    visited = set()
    for start in data:
        if start not in visited:
            ans += 1
            dfs(data, start, visited)
    return ans


def parse_data(data):
    graph = defaultdict(list)
    for line in data:
        a = re.findall(r'\d+', line)
        graph[a[0]] = a[1:]
    return graph


data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
