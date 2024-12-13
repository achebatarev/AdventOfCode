from dataclasses import dataclass
g = list(map(list, open('input.d6').read().splitlines()))
from copy import deepcopy
from time import sleep
# TODO: keep track of guards position and the direction, and check if he can move forward or not
import itertools


class LeavingLocationException(Exception):
    ...

@dataclass
class P:
    y: int 
    x: int

def can_move(grid, p: P, d: P) -> bool:
    if 0 <= p.y + d.y < len(grid) and 0 <= p.x + d.x < len(grid[0]):
        return grid[p.y + d.y][p.x + d.x] != '#'  
    raise LeavingLocationException

def move(grid, p: P, d: P):
    ngrid = deepcopy(grid)
    ngrid[p.y][p.x] = 'V' 
    ngrid[p.y + d.y][p.x + d.x] = '^'
    return ngrid, P(p.y + d.y, p.x + d.x) 

def turn(d):
    return P(d.x, -d.y)

def find_char(grid) -> P:
    for y, line in enumerate(grid):
        for x, e in enumerate(line):
            if e == '^':
                return P(y, x)
    raise Exception

def part1(grid):
    pos = find_char(grid)
    direction = P(-1, 0) # (-1, 0) -> (0, 1) -> (1, 0) -> (0, -1)
    while True:
        try:
            if can_move(grid, pos, direction):
                grid, pos = move(grid, pos, direction)
                # sleep(0.2)
                # __import__('pprint').pprint(grid)
            else: 
                direction = turn(direction)
        except LeavingLocationException:
            return sum(1 if grid[y][x] == 'V' else 0 for y, x in itertools.product(range(len(grid)), range(len(grid[0])))) + 1

print(part1(deepcopy(g)))


