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
    with open(filename, 'r') as f:
        return f.read()


# I can create functions for each instruction type, and then simply handle it in there
# or simply use if statments, the same thing will be achieved
# I also need to track the dictionary of where programs located to support exchange in O(1)
def execute_instruction(arr, instruction):
    if instruction.startswith('s'):
        x = int(re.findall(r'\d+', instruction)[0])
        return arr[-x:] + arr[:-x]
    elif instruction.startswith('x'):
        a, b = map(int, re.findall(r'\d+', instruction))
        arr[a], arr[b] = arr[b], arr[a]
        return arr
    elif instruction.startswith('p'):
        A, B = instruction[1], instruction[3]
        a, b = arr.index(A), arr.index(B)
        arr[a], arr[b] = arr[b], arr[a]
        return arr


def partA(data):
    arr = list(map(chr, range(ord('a'), ord('p') + 1)))
    for instruction in data:
        arr = execute_instruction(arr, instruction)
    return ''.join(arr)


# there could be a repetition, which would help quite a lot
# I can simply get the index of where the first repetition occured, and then I just will be left with wlaking th remainder between total and me number, easy pz
def partB(data):
    arr = list(map(chr, range(ord('a'), ord('p') + 1)))
    k = 1000000000
    d = {}
    freedom = 0
    for i in range(k):

        #        if i % 10000000 == 0:
        #print(f'{i}/{k}')

        a = ''.join(arr)

        if a in d:
            freedom = i
            break

        for instruction in data:
            arr = execute_instruction(arr, instruction)

        d[a] = i

    for key, val in d.items():
        if val == (k % freedom):
            return key

    return ''.join(arr)


def parse_data(data):
    return data.split(',')


if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(partA(parsed_data))
    print(partB(parsed_data))
