import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
import math
from dataclasses import dataclass
import re
from typing import Dict

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


def partA(graph):
    inbound = defaultdict(int)
    for root, children in graph.items():
        for child in children:
            inbound[child] += 1

    for root in graph:
        if inbound[root] == 0:
            return root


def dfs(graph, node):
    global weights, ans
    weight = weights[node]
    t = defaultdict(list)
    for child in graph[node]:
        w = dfs(graph, child)
        t[w].append(child)
        weight += w

    if len(t) > 1 and not ans:
        normal = max(t.items(), key=lambda x: len(x[1]))
        culprit = min(t.items(), key=lambda x: len(x[1]))
        ans = weights[culprit[1][0]] + (normal[0] - culprit[0])

    return weight


def partB(root, graph):
    global ans
    ans = 0
    dfs(graph, root)
    return ans


def parse_data(data):
    global weights
    graph = {}
    weights = {}
    for line in data:
        programs = re.findall(r'\b[a-z]+\b', line)
        d = int(re.findall(r'\d+', line)[0])
        root = programs[0]
        graph[root] = programs[1:]
        weights[root] = d
    return graph


data = read_data(FILE)
parsed_data = parse_data(data)
ansA = partA(parsed_data)
print(ansA)
print(partB(ansA, parsed_data))
