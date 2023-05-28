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
        return int(f.read().strip())
    return data


def partA(n):
    arr = [0]
    i = 0
    for v in range(1, 2018):
        i = (((n % len(arr)) + i) % len(arr)) + 1
        arr.insert(i, v)
        #print(arr, i, v)
    return arr[(i + 1) % len(arr)]



def partB(n):
    k =  50000000
    i = 0
    ans = 0
    for v in range(1,k):

        i = (((n % v) + i) % v) + 1

        if i == 1:
            ans = v

    return ans 


def parse_data(data):
    return data


if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(partA(parsed_data))
    print(partB(parsed_data))
