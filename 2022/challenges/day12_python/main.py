import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
from dataclasses import dataclass
import time

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'


@dataclass
class Point:
    y: int
    x: int


def read_data(filename: str):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(list(line.strip()))
    return data


def bfs(data, p):
    global goal
    m, n = len(data), len(data[0])
    seen = [[False] * n for _ in range(m)]
    q = deque([p])
    steps = 0
    seen[p.y][p.x] = True
    moves = [(0, 1), (-1, 0), (1, 0), (0, -1)]
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            elevation = data[node.y][node.x]
            if node == goal:
                return steps
            for r, c in moves:
                y, x = node.y + r, node.x + c
                if y < m and y >= 0 and x < n and x >= 0 and not seen[y][x]:
                    if ord(data[y][x]) - ord(elevation) <= 1:
                        seen[y][x] = True
                        q.append(Point(y, x))
        steps += 1
    return -1


def partA(data) -> int:
    p = find_char_pos(data, 'S')
    data[p.y][p.x] = 'a'
    return bfs(data, p)


def partB(data):
    result = float('inf')
    for i, line in enumerate(data):
        for j, e in enumerate(line):
            if e == 'a':
                out = bfs(data, Point(i, j))
                if out != -1:
                    result = min(out, result)
    return result


def find_char_pos(arr, char):
    for i, line in enumerate(arr):
        for j, e in enumerate(line):
            if e == char:
                return Point(i, j)
    return Point(0, 0)


def parse_data(data):
    global goal
    goal = find_char_pos(data, 'E')
    data[goal.y][goal.x] = 'z'
    return data


data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
