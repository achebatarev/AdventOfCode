import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
from dataclasses import dataclass
import heapq
from math import gcd

try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'

@dataclass
class Node:
    L: str 
    R: str
    
def read_data(filename: str):
    with open(filename, 'r') as f:
        return f.read().splitlines()

def first(data):
    directions, d = data
    node = 'AAA'
    steps = 0
    while node != 'ZZZ':
        direction = directions[steps%(len(directions))]
        node = getattr(d[node], direction)
        steps += 1 
    
    return steps 


def find_loop(node, graph, directions):
    steps = 0
    while node[-1] != 'Z':
        direction = directions[steps%(len(directions))]
        node = getattr(graph[node], direction)
        steps += 1
    return steps


def second(data):
    directions, d = data
    q = [e for e in d if e[-1] == 'A']
    lcm = 1
    a = []
    for node in q:
        a.append(find_loop(node, d, directions))

    for i in a:
        lcm = lcm*i//gcd(lcm, i)

    return lcm 

def parse_data(data):
    directions = data[0]
    d = {}
    for line in data[2:]:
        e = line.split('=')
        d[e[0].strip()] = Node(e[1].split(',')[0][2:], e[1].split(',')[1][1:-1])

    return directions, d

if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(first(parsed_data))
    print(second(parsed_data))
