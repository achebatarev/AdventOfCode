import sys
import math
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
from dataclasses import dataclass
from tkinter import W

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'


def read_data(filename: str):
    with open(filename, 'r') as f:
        return int(f.read().strip())


# right bottom corner is a square, so I can just calculate x, y of it
# now I need to identify the layer that I am on
# 1:1, 3:2, 5:3, 7:4, 9:5, 11:6, 13
# I got odd squares
# also, I know the size of the current layer
# okay, now I can easily search for x, y
# the only thing to left to identify is my current y, x
# I got certain radius, using binary search I can idenitfy how far is the corner from center, but it is irrelevent
# if I know layer, x, y is easy to identify, since it is simply, that layer in both y and x, and layer is simply current corner + 1
# then I can walk to the left k steps and then up k steps, if I still do not find, I have to walk k -1 and k - 1
# I know that it is in vicinity of me, and each size will be k - 1
# very easy to simply walk it recording my x and y change
# can I do without walking it
# first I subtract, x, then I subtract y, then I add x and then I add y
# left top corner, has the reversed coordinaters of the bottom-right corner. So if I figure out math how to find position in that half, extending for other half would be trivial
# so I find difference between them and then I just use modulo
def partA(n):
    k = math.ceil(math.sqrt(n))
    diff = (k * k) - n
    return diff
    print(diff)
    quadrant = diff // (k - 1)
    print(quadrant)
    return distance - (diff % (k - 1))


# I just need to identify whre my input is located in x, y space relative to the center and then I just find taxicab distance
# 1 1 2 2 3 3 4 4
# I can identify on which layer I will be
#But how will this help me with identifying my x and y coordinates relative to
# I can build a matrix, but I do not wanna do that
# 0, 1 : -1, 0 : 0, -1 : 1, 0 : 0, 1
# r, c : -c, r : -c, r : -r, -c:
# so I got, y, x, r, c, layer, num I can create a function using all of the above as parametrs, is there a way to decrease number of parametrs
def brute_force_partA(data):
    t = 20
    matrix = [[None] * t for _ in range(t)]
    n, m = len(matrix[0]), len(matrix)
    layer = 1
    start_y, start_x = m // 2, n // 2
    y, x = start_y, start_x
    num = 2
    run = False
    matrix[y][x] = 1
    r, c = 0, 1
    while True:
        for _ in range(2):
            for _ in range(layer):
                y += r
                x += c

                try:
                    matrix[y][x] = num
                except:
                    run = True
                num += 1

            r, c = -c, r

        if run:
            break
        #print(y, x)

        layer += 1
    #pprint(matrix)
    res = 0
    for i, line in enumerate(matrix):
        for j, e in enumerate(line):
            if e:
                print(e, end='\t')
            if e == data:
                res = abs(start_y - i) + abs(start_x - j)
        print()
    return res


def partB(data):
    print('PartB')
    t = 1000
    matrix = [[0] * t for _ in range(t)]
    n, m = len(matrix[0]), len(matrix)
    layer = 1
    start_y, start_x = m // 2, n // 2
    y, x = start_y, start_x
    num = 2
    run = False
    matrix[y][x] = 1
    moves = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1),
             (1, -1)]
    r, c = 0, 1
    while True:
        for _ in range(2):
            for _ in range(layer):
                y += r
                x += c
                try:
                    num = 0
                    for i, j in moves:
                        num += matrix[y + i][x + j]
                    if num > data:
                        return num
                    matrix[y][x] = num
                except:
                    run = True
            c, r = -r, c
        if run:
            break

        layer += 1


def parse_data(data):
    return data


data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
