# the largest element so far is visible 
import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import itertools
import heapq

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

#given ranges to iterate over, iterate and fill up the visible 2d array
def iterate(data, visible, range1, range2, limit=0, vertical=False) -> None:
    for i, j in itertools.product(range1, range2):
        #reset the height of the biggest tree so far
        if j == limit: big = -1 
        if vertical: i, j = j, i
        tree = int(data[i][j])
        if tree > big:
            visible[i][j] = True
            big = tree 

def partA(data) -> int:
    visible = [[False] * len(data[0]) for _ in range(len(data))]
    iterate(data, visible, range(len(data)), range(len(data[0])))
    iterate(data, visible, range(len(data)), range(len(data[0])-1, -1, -1), len(data)-1)
    iterate(data, visible, range(len(data[0])), range(len(data)), 0, True)
    iterate(data, visible, range(len(data[0])), range(len(data)-1, -1, -1), len(data)-1, True)

    return sum(sum(visible, []))

def partB(data) -> int:
    result = 0
    moves = [(1,0), (0,1), (-1, 0), (0, -1)]
    for i, line in enumerate(data):
        for j, tree in enumerate(line):
            score = 1
            for r, c in moves:
                y, x, n = i+r, j+c, 0
                while y < len(data) and x < len(line) and y >= 0 and x >= 0:
                    n += 1
                    if tree <= data[y][x]: break
                    y, x = y+r, x+c
                score *= n 
            result = max(score, result)

    return result 

def parse_data(data):
    return data

data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
