import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
import math
from dataclasses import dataclass
import operator
import functools
import binascii

sys.path.append('../')
from day_10.main import partB as knot_hash

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'


def read_data(filename: str):
    with open(filename, 'r') as f:
        return f.read().strip()


def count_bits(n):
    ans = 0
    while n:
        n = n & (n - 1)
        ans += 1
    return ans


def partA(data):
    ans = 0
    for i in range(128):
        n = int(knot_hash(f'{data}-{i}'), 16)
        ans += count_bits(n)
    return ans


moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dfs(graph, y, x, visited):
    if not (0 <= y < len(graph) and 0 <= x < len(graph[0])):
        return
    if graph[y][x] == '.' or visited[y][x]:
        return
    visited[y][x] = True
    for r, c in moves:
        dfs(graph, y + r, x + c, visited)


# padding is off
def partB(data):
    matrix = [['.'] * 128 for _ in range(128)]
    visited = [[False] * 128 for _ in range(128)]
    for i in range(128):
        h = knot_hash(f'{data}-{i}')
        n = int(h, 16)
        if i == 3:
            #print(binascii.unhexlify(h))
            print(h, hex(n))
            print(len('{0:0128b}'.format(n)), len(str(bin(n))[2:]))
            print(bin(n), '{0:0128b}'.format(n))
        for j, e in enumerate('{0:0128b}'.format(n)):
            if e == '1':
                matrix[i][j] = '#'
    ans = 0
    res = 0
    for i, line in enumerate(matrix):
        for j, cell in enumerate(line):
            if cell == '#':
                res += 1
            if not visited[i][j] and cell == '#':
                #if j == 0:
                #for lin in matrix:
                #for c in lin:
                #print(c, end=' ')
                #print()
                dfs(matrix, i, j, visited)
                ans += 1
    return ans


def parse_data(data):
    return data


data = read_data(FILE)
parsed_data = parse_data(data)
#print(partA(parsed_data))
print(partB(parsed_data))
