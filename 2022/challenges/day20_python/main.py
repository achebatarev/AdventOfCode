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

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'


def read_data(filename: str):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(int(line.strip()))
    return data

# I need to create a list of unique elements, and map each of the elements 
# to that unique element
def partA(data):
    mappingA = {}
    mappingB = {}
    n = len(data)
    for i, e in enumerate(data):
        mappingA[e] = i
        mappingB[i] = e

    arr = list(range(len(data)))
    print(arr)
    for e in data:
        i = arr.index(mappingA[e])
        arr.insert((i + e) % n, mappingA[e])
        arr.pop(i)
    print(arr)
    loc = arr.index(mappingA[0])
    return sum((mappingB[arr[(loc + 1000)%n]], mappingB[arr[(loc+2000)%n]], mappingB[arr[(loc+3000)%n]]))


    pass


def partB(data):
    pass


def parse_data(data):
    return data


if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(partA(parsed_data))
    print(partB(parsed_data))
