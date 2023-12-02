import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
from dataclasses import dataclass
import heapq

from itertools import chain 
            

try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'

@dataclass
class Cube:
    amount: int
    color: str 

def read_data(filename: str):
    with open(filename, 'r') as f:
        return f.read().splitlines()

def first(data):
    mapping = {'green': 13, 'red': 12, 'blue': 14}
    ans = 0
    for i, games in data.items():
        win = True

        for s in games:
            m = {'green': 0, 'red': 0, 'blue': 0}
            for cube in s:
                m[cube.color] += int(cube.amount)

            for color in m:
                if m[color] > mapping[color]:
                    win = False

        if win:
            ans += i

    return ans


def second(data):
    mapping = {'green': 13, 'red': 12, 'blue': 14}

    res = 0
    for _, games in data.items():
        
        ans = {'green': 0, 'red': 0, 'blue': 0}
        for s in games:
            m = {'green': 0, 'red': 0, 'blue': 0}
            for cube in s:
                m[cube.color] += int(cube.amount)

            for color in m:
                ans[color] = max(m[color], ans[color])
        t = 1
        for _, b in ans.items():
            t *= b
        res += t

    return res 

def parse_data(data):
    l = {}
    for e in data:
        game, info = e.split(':')
        l[int(game.split()[1])] = [[Cube(*c.strip().split()) for c in a.split(',')] for a in info.split(';')]
    return l 

if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(first(parsed_data))
    print(second(parsed_data))
