from tqdm import tqdm
from dataclasses import dataclass
g = list(map(list, open('input.d6').read().splitlines()))
from copy import deepcopy
from time import sleep
# TODO: keep track of guards position and the direction, and check if he can move forward or not
import itertools


class LeavingLocationException(Exception):
    ...

@dataclass(frozen=True)
class P:
    y: int 
    x: int

def can_move(grid, p: P, d: P) -> bool:
    if 0 <= p.y + d.y < len(grid) and 0 <= p.x + d.x < len(grid[0]):
        return grid[p.y + d.y][p.x + d.x] != '#'  
    raise LeavingLocationException

def move(ngrid, p: P, d: P):
    ngrid[p.y][p.x] = 'V' 
    ngrid[p.y + d.y][p.x + d.x] = '^'
    return P(p.y + d.y, p.x + d.x) 

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
                pos = move(grid, pos, direction)
            else: 
                direction = turn(direction)
        except LeavingLocationException:
            return sum(1 if grid[y][x] == 'V' else 0 for y, x in itertools.product(range(len(grid)), range(len(grid[0])))) + 1

# TODO: capture the loop
def run_game(grid, pos, direction):
    s = set()
    while True:
        try:
            if can_move(grid, pos, direction):
                pos = move(grid, pos, direction)
            else: 
                direction = turn(direction)

            if (pos, direction) in s:
                return False
            s.add((pos, direction))

        except LeavingLocationException:
            return True 

def place_obstacle(grid, p):
    ngrid = deepcopy(grid)
    ngrid[p.y][p.x] = '#' 
    return ngrid



# TODO: the idea is simple, we run the game and check if we left, I need a way to identify the loop thou
def part2(grid):
    ans = 0
    pos = find_char(grid)
    direction = P(-1, 0) # (-1, 0) -> (0, 1) -> (1, 0) -> (0, -1)
    for y, line in tqdm(enumerate(grid), total=len(grid)):
        for x, e in enumerate(line):
            if e not in ('#', '^'):
                obstacle_grid = place_obstacle(grid, P(y, x))
                if not run_game(obstacle_grid, pos, direction):
                    ans += 1
    return ans



print('Part1', part1(deepcopy(g)))
print('Part2', part2(deepcopy(g)))



