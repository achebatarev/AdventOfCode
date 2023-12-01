import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
from typing import List

try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'

def read_data(filename: str):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data

def calc(char: str):
    # can be a one liner, but readability for the win
    if char.islower():
        return (ord(char) - ord('a')) + 1
    else:
        return (ord(char) - ord('A')) + 27

def partA(data: List[str]):
    result = 0
    for r in data:
        mid = len(r) // 2
        s = set(r[:mid])
        char = list(s.intersection(set(r[mid:])))[0]
        result += calc(char)
    return result

def partB(data: List[str]):
    result = 0
    for i in range(0, len(data), 3):
        # readability is for the weak
        result += calc(list(set(data[i]).intersection(set(data[i+1]).intersection(set(data[i+2]))))[0])
    return result

def parse_data(data):
    return data

data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
