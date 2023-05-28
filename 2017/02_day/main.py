import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
from dataclasses import dataclass

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'


def read_data(filename: str):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(list(map(int, line.strip().split())))
    return data


def partA(data):
    return sum(max(e) - min(e) for e in data)


#only 2 numbers that are divisible by each other
# meaning there ther gcd != 1, and that they are no coprimes
# I can easily find what they are divisible by, and then, simply, check each number if they are divisible by it or not
#
def partB(data):
    res = 0
    for e in data:
        for n in e:
            for m in e:
                if n <= m:
                    continue
                if n % m == 0:
                    res += n // m
    return res


def parse_data(data):
    return data


data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
