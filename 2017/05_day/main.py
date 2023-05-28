import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
import math
from dataclasses import dataclass
from tkinter import Tk

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'


def read_data(filename: str):
    with open(filename, 'r') as f:
        return list(map(int, f.read().splitlines()))


# so we just need to jump out of the list size
def partA(data):
    data = data.copy()
    i = 0
    step = 0
    while i < len(data):
        n = data[i]
        data[i] += 1
        i += n
        step += 1
    return step


def partB(maze):
    n = 0
    step = 0
    while n >= 0 and n < len(maze):
        if maze[n] >= 3:
            maze[n] -= 1
            n = n + maze[n] + 1
        else:
            maze[n] += 1
            n = n + maze[n] - 1
        step += 1
    return step


def parse_data(data):
    return data


data = read_data(FILE)
parsed_data = parse_data(data)
ansA = partA(parsed_data)
print(ansA)
ansB = partB(parsed_data)
print(ansB)
if ansA:
    Tk().clipboard_append(str(ansA))

if ansB:
    Tk().clipboard_append(str(ansA))
