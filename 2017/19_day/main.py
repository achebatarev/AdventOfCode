import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
import math
from dataclasses import dataclass
import operator
import functools
import re
import time
from copy import copy

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
        return f.read().splitlines()

# TODO: improve to support finding different entrances
def find_entrance(arr):
    for y, line in enumerate(arr):
        for x, cell in enumerate(line):
            if cell == '|':
                return Point(y, x)
    return Point(0, 0) 

# how do I decide if I need to go up or down? Try both
# there is always just one way to go, so that makes it easier

# Decide which direction I need to go 
# follow that line until hitting +
# TODO: identify when to break
#TODO: handle edge cases
# NOTE: only adding A now:w
def bounds(arr, p: Point) -> bool:
    if p.y < 0 or p.y >= len(arr) or p.x < 0 or p.x >= len(arr[0]):
        return False
    return True

def partA(arr):
    pos = find_entrance(arr)
    ans = []
    i = 0
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while True:
        for j, (r, c) in enumerate(moves):
            p = Point(pos.y+r, pos.x+c) 

            if i % 2 == 0 and j in (0, 1):
                continue

            if i % 2 != 0 and j in (2, 3):
                continue

            if not bounds(arr, p):
                continue

            while bounds(arr, p) and (arr[p.y][p.x] in ('-', '|') or arr[p.y][p.x].isalpha()):
                if arr[p.y][p.x].isalpha():
                    ans += arr[p.y][p.x]
                p.y += r
                p.x += c
            
            if Point(pos.y+r, pos.x+c) != p:
                break

        pos = copy(p)
        #print(pos, arr[pos.y][pos.x])
        i += 1

        if arr[pos.y][pos.x] != '+':
            break

    return ''.join(ans)


def partB(arr):
    pos = find_entrance(arr)
    ans = 0 
    i = 0
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while True:
        for j, (r, c) in enumerate(moves):
            p = Point(pos.y+r, pos.x+c) 

            if i % 2 == 0 and j in (0, 1):
                continue

            if i % 2 != 0 and j in (2, 3):
                continue

            if not bounds(arr, p):
                continue

            while bounds(arr, p) and (arr[p.y][p.x] in ('-', '|') or arr[p.y][p.x].isalpha()):
                p.y += r
                p.x += c
                ans += 1
            
            if Point(pos.y+r, pos.x+c) != p:
                ans += 1
                break

        pos = copy(p)
        #print(pos, arr[pos.y][pos.x])
        i += 1

        if arr[pos.y][pos.x] != '+':
            break

    return ans 

def parse_data(data):
    return data


if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(partA(parsed_data))
    print(partB(parsed_data))
