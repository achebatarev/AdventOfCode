import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
from dataclasses import dataclass
import heapq
import math
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
            data.append(line.strip())
    return data


def mult(n, factor, mask):
    prod = factor * n
    result = (prod & mask) + (prod >> 31)
    return result - mask if result >> 31 else result


def generator(n, factor, div=1):
    mod = 2147483647
    mask = 0xFFFF
    while True:
        n = mult(n, factor, 0x7FFFFFFF)
        if n % div == 0:
            yield n & mask


def partA(data):
    A, B = data
    factorA, factorB = 16807, 48271
    ga, gb = generator(A, factorA), generator(B, factorB)
    return sum(next(ga) == next(gb) for _ in range(40000000))


def partB(data):
    A, B = data
    factorA, factorB = 16807, 48271
    mod = 2147483647
    mask = 0xFFFF
    ans = 0
    for _ in range(5000000):
        A = (factorA * A) % mod
        B = (factorB * B) % mod

        while A % 4 != 0:
            A = (factorA * A) % mod
        while B % 8 != 0:
            B = (factorB * B) % mod

        if ((A & mask) ^ (B & mask)) == 0:
            ans += 1
    return ans


def parse_data(data):
    pair = []
    for line in data:
        pair.append(int(re.findall(r'\d+', line)[0]))
    return pair


data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
