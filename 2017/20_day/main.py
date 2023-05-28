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
from copy import deepcopy

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'

@dataclass
class Point:
    x: int
    y: int
    z: int

@dataclass
class Particle:
    p: Point 
    v: Point 
    a: Point 

def read_data(filename: str):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data

def tick(particle):
    particle.v.x += particle.a.x
    particle.v.y += particle.a.y
    particle.v.z += particle.a.z
    particle.p.x += particle.v.x
    particle.p.y += particle.v.y
    particle.p.z += particle.v.z

def distance(p):
    return abs(p.p.x) + abs(p.p.y) + abs(p.p.z)

def partA(data):
    data = deepcopy(data)
    for _ in range(1000):
        winner = (float('inf'), 0)
        for i, particle in enumerate(data):
            tick(particle)
            winner = min(winner, (distance(particle), i), key=lambda x: x[0])
    return winner[1]

def partB(data):
    data = list(enumerate(data))
    for _ in range(1000):
        d = defaultdict(int) 
        for i, particle in data:
            tick(particle)
            d[str(particle.p)] += 1

        data = [(i, particle) for i, particle in data if d[str(particle.p)] <= 1]
    return len(data)


def parse_data(data):
    l = []
    for line in data:
        ints = re.findall(r'-?\d+', line)
        points = []
        for i in range(0, len(ints), 3):
            points.append(Point(*map(int, ints[i:i+3])))
        l.append(Particle(*points))
    return l 


if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(partA(parsed_data))
    print(partB(parsed_data))
