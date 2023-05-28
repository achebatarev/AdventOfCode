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
    ITER = 5
    FILE = sys.argv[1] 
except:
    ITER = 2
    FILE = 'test.in'

def read_data(filename: str):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data

def split(arr):
    n = len(arr)
    new_arr = [[None]*(2*n) for _ in range(2*n)]     
    for y, line in enumerate(arr):
        for x, square in enumerate(line):
            sq1 = [square[0][:2], square[1][:2]]
            sq2 = [square[0][2:], square[1][2:]]
            sq3 = [square[2][:2], square[3][:2]]
            sq4 = [square[2][2:], square[3][2:]]

            new_arr[y*2][x*2] = sq1
            new_arr[(y*2)][(x*2)+1] = sq2
            new_arr[(y*2)+1][(x*2)] = sq3
            new_arr[(y*2)+1][(x*2)+1] = sq4
    pprint(new_arr)
    return new_arr

def transform(arr, mapping):
    new_arr = []
    for line in arr:
        new_line = []
        for square in line:
            if tuple(square) not in mapping:
                pprint(arr)
                pprint(square)
                raise Exception('Pattern is missing')
            new_line.append(mapping[tuple(square)])
        new_arr.append(new_line)
    return new_arr

# this entire problem is about splitting square into smaller squares and identifying which rule to apply to each, and the combining it all together
# 3, 4, 6, 9,  
# FIX: 4 and 6 are both even, so gotta be splitting them  
def partA(mapping):
    squares = [[['.#.', '..#', '###']]]
    #pprint(mapping)
    for i in range(ITER):
        print(i, 'iteration')
        pprint(squares)
        if i % 2 != 0:
            squares = split(squares)
        squares = transform(squares, mapping)
    ans = 0 
    for line in squares:
        for square in line:
            for cell in square:
                ans += cell.count('#')
    pprint(squares)
    return ans

def partB(data):
    pass

def rotate(arr):
    new_arr = list(map(''.join, map(reversed, zip(*arr))))
    return new_arr

def h_flip(arr):
    new_arr = list(map(''.join, map(reversed, arr)))
    return new_arr

def v_flip(arr):
    new_arr = list(map(''.join, zip(*map(reversed, zip(*arr)))))
    return new_arr 

def parse_data(data):
    ttt = []
    rules = {} 
    for rule in data:
        inn, out = rule.split('=>')
        square = inn.strip().split('/')
        # will need to rotate and flip our input square to cover all of the cases
        ttt.append(tuple(square) in rules)
        for _ in range(4):
            rules[tuple(square)] = out.strip().split('/')
            rules[tuple(h_flip(square))] = out.strip().split('/')
            rules[tuple(v_flip(square))] = out.strip().split('/')
            square = rotate(square)
    return rules 

if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(partA(parsed_data))
    print(partB(parsed_data))
