import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
from dataclasses import dataclass
import heapq

try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'


def read_data(filename: str):
    with open(filename, 'r') as f:
        return f.read().splitlines()

def first(data):
    time, distance = data
    ans = 1 
    for t, dist in zip(time, distance):
        res = 0
        for i in range(1, t):
            a = i * (t - i)
            if a > dist:
                res += 1
        ans *= res
    return ans

def second(data):
    time, distance = data
    time = int(''.join(map(str, time)))
    distance = int(''.join(map(str, distance)))
    res = 0
    for i in range(1, time):
        a = i * (time - i)
        if a > distance:
            res += 1
    return res 

def parse_data(data):
    time = list(map(int, data[0].split()[1:]))
    distance = list(map(int, data[1].split()[1:]))
    return time, distance 

if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(first(parsed_data))
    print(second(parsed_data))
