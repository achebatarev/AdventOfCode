from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass
import sys
try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'

@dataclass(frozen=True)
class P:
    y: int
    x: int

    def __add__(self, other: "P"):
        return P(self.y + other.y, self.x + other.x)


grid = list(map(list, open(FILE).read().splitlines()))

def part1(grid):
    d = defaultdict(list)
    s = set()
    for y, line in enumerate(grid):
        for x, e in enumerate(line):
            if e != '.':
                for p in d[e]:
                    s.add(P(p.y + (p.y - y), p.x + (p.x - x)))
                    s.add(P(y + (y - p.y), x + (x - p.x)))
                d[e].append(P(y, x))
    ans = set() 
    for p in s: 
        if 0 <= p.y < len(grid) and 0 <= p.x < len(grid[0]):
            ans.add(p)
    # NOTE: to vizualize map
    # for y, line in enumerate(grid):
    #     for x, e in enumerate(line):
    #         if e == '.' and P(y, x) in s:
    #             grid[y][x] = '#'

    return len(ans)

def part2(grid):
    d = defaultdict(list)
    s = set()
    for y, line in enumerate(grid):
        for x, e in enumerate(line):
            if e != '.':
                # TODO: now every signal is propogated
                # I need to capture every signal and how it's propogated
                # Then I can use math to calculate how long it'll be propataged for
                # the problem with math is overlaps
                for p in d[e]:
                    s.add((P(y, x), P(p.y - y, p.x - x)))
                    s.add((P(p.y, p.x), P(y - p.y, x - p.x)))
                d[e].append(P(y, x))

    ans = set() 
    for p, direction in s: 
        pd = p + direction
        while 0 <= pd.y < len(grid) and 0 <= pd.x < len(grid[0]):
            ans.add(pd)
            pd += direction
    
    return len(ans)

print(part1(deepcopy(grid)))
print(part2(deepcopy(grid)))

