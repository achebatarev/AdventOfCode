import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
from dataclasses import dataclass
import heapq
import sys
sys.setrecursionlimit(10**6)

try:
    FILE = sys.argv[1]
except:
    FILE = "test.in"


def read_data(filename: str):
    with open(filename, "r") as f:
        return f.read().splitlines()


# questions:
# How to identify where to move from a start position
# how to traverse the graph
def traverse(mapping, 
             arr, 
             y, 
             x, 
             visited):
    start = True
    steps = 0
    big_boy = None
    try:
        big_boy = max(max(e for e in line if e is not None) for line in visited if any(line))
    except Exception:
        ...
        
    while arr[y][x] != "S" or start:
        current_element = arr[y][x]
        for r, c in mapping[current_element]:
            yr, xc = y + r, x + c
            if y + r >= len(arr) or y + r < 0 or x + c >= len(arr[0]) or x + c < 0:
                continue
            visited_val = visited[yr][xc] 
            if current_element == "S" and not any(
                y == y + r + r1 and x == x + c + c1
                for r1, c1 in mapping[arr[y + r][x + c]]
            ):
                continue
            if visited_val is not None and visited_val < steps:
                continue
            if start and visited_val != big_boy:
                continue
            visited[y][x] = steps
            y, x = yr, xc
            steps += 1
            break
        else: 
            break
        start = False
    visited[y][x] = steps


def first(arr):
    visited = [[None] * len(arr[0]) for _ in range(len(arr))]
    clockwise = {
        "J": (0, -1),
        "F": (0, 1),
        "L": (-1, 0),
        "7": (1, 0),
        "|": (1, 0),
        "-": (0, 1),
    }
    counter_clockwise = {
        "J": (-1, 0),
        "F": (1, 0),
        "L": (0, 1),
        "7": (0, -1),
        "|": (-1, 0),
        "-": (0, -1),
    }
    mapping = {
        k: [v, v1]
        for (k, v), (_, v1) in zip(clockwise.items(), counter_clockwise.items())
    }
    mapping["S"] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    mapping["."] = []
    for y, line in enumerate(arr):
        x = line.find("S")
        if x == -1:
            continue
        traverse(mapping, arr, y, x, visited)
        traverse(mapping, arr, y, x, visited)
    return max(max(e for e in line if e is not None) for line in visited if any(line))

# landfill
def landfill(arr, y, x, var):
    if y >= len(arr) or y < 0 or x >= len(arr[0]) or x < 0:
        return 
    if arr[y][x] is not None:
        return 
    moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    arr[y][x] = var 
    for r, c in moves:
        landfill(arr, y+r, x+c, var)

def pad(arr):
    arr = [[None] + line + [None] for line in arr]
    arr = [[None] * len(arr[0])] + arr + [[None] * len(arr[0])]
    return arr

# I just need to find a spot withing a loop, then I can easily run a landfill algorithm
# or simply run landfill twice
def second(arr):
    visited = [[None] * len(arr[0]) for _ in range(len(arr))]
    clockwise = {
        "J": (0, -1),
        "F": (0, 1),
        "L": (-1, 0),
        "7": (1, 0),
        "|": (1, 0),
        "-": (0, 1),
    }
    counter_clockwise = {
        "J": (-1, 0),
        "F": (1, 0),
        "L": (0, 1),
        "7": (0, -1),
        "|": (-1, 0),
        "-": (0, -1),
    }
    mapping = {
        k: [v, v1]
        for (k, v), (_, v1) in zip(clockwise.items(), counter_clockwise.items())
    }
    mapping["S"] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    mapping["."] = []
    for y, line in enumerate(arr):
        x = line.find("S")
        if x == -1:
            continue

        traverse(mapping, arr, y, x, visited)
        traverse(mapping, arr, y, x, visited)

    visited = pad(visited)
    landfill(visited, 0, 0, 'O')

    for y, line in enumerate(visited):
        for x, e in enumerate(line):
            if e is None:
                landfill(visited, y, x, "I")

    return sum(line.count('I') for line in visited )


def parse_data(data):
    return data


if __name__ == "__main__":
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(first(parsed_data))
    print(second(parsed_data))
