import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
from dataclasses import dataclass
import heapq
from copy import deepcopy
from functools import cache

try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'


def read_data(filename: str):
    with open(filename, 'r') as f:
        return f.read().splitlines()

def first(data: list[str]) -> int:
    arr = [list(e) for e in data]
    arr = run(arr)
    return calculate(arr)

def can_move(arr: list[list[str]], y: int, x: int, direction: tuple[int, int] = (-1, 0)) -> bool:
    r, c = direction
    n_y, n_x  = y + r, x + c
    if n_y < 0  or n_y >= len(arr) or n_x < 0 or n_x >= len(arr[0]) or arr[n_y][n_x] != '.':
        return False
    return True

def run(arr: list[list[str]], direction: tuple[int, int]=(-1, 0)) -> list[list[str]]:
    no_moves = False
    r, c = direction
    while not no_moves:
        no_moves = True
        for i, line in enumerate(arr):
            for j, e in enumerate(line):
                if e == 'O' and can_move(arr, i, j, direction):
                    arr[i][j] = '.'
                    arr[i+r][j+c] = 'O'
                    no_moves = False
    return arr

def calculate(arr) -> int:
    ans = 0
    for i, line in enumerate(arr):
            ans += line.count('O') * (len(arr) - i)
    return ans 


@cache
def run_cycle(arr: tuple[tuple[str]]) -> tuple[tuple[str]]:
    new_arr = [list(e) for e in arr] 
    moves = ((-1, 0), (0, -1), (1, 0), (0, 1))
    for move in moves:
        new_arr = run(new_arr, move)
    l = tuple(tuple(e) for e in new_arr)
    return l

def second(data, cycle=1_000_000_000):

    arr = tuple(tuple(e) for e in data)
    warmed = False
    total = 0
    for i in range(cycle):
        if i % 2000 == 0 and i != 0:
            total = max(total, run_cycle.cache_info().currsize)
            loop_size = run_cycle.cache_info().currsize 
            run_cycle.cache_clear()
            if warmed:
                break
            warmed = True

        arr = run_cycle(arr)
    diff = total - loop_size
    ans_position = (cycle-diff) % loop_size
    arr = tuple(tuple(e) for e in data)

    for i in range(ans_position+diff):
        arr = run_cycle(arr)

    return calculate(arr)

def parse_data(data: list[str]) -> list[str]:
    return data 

if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(first(parsed_data))
    print(second(parsed_data))
