import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
from dataclasses import dataclass
import bisect
import copy

try:
    FILE = sys.argv[1]
    K = 300
    N, M = 700-K, 170
except:
    FILE = 'test.in'
    K = 480
    N, M = 530-K, 12

@dataclass
class Point:
    x: int
    y: int


def read_data(filename: str):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data


# it just needs to return the y of an obstacle
# if no obstacle in the way, I just return -1
def find_first(data, p):
    n, m = len(data[0]), len(data)
    for i in range(p.y + 1, m):
        if data[i][p.x] != '.':
            return i
    return -1


# Supposed to happen:
# I set a sand at the certain point
# then I check if there is 3 obstacles direcly below, if not
# then we can fit a block, in one of the spots
# we check the closest obstacle to my crurrent sand position, directly below
# obstacle postion - 1 is our new position of y for the sand_block
# then we check if we two block to the left are free, if that is so, we find fisrt obstacle there
# and move our sand there
# do the same with the right taking in account a new position of our sand
# Problem:
# the current sand gets dispatched to the left and right
# I should break out of the loop, if obstacle not found, if all elements underneath are not . and no moves were made this turn
# after moving a block I need to reset the order of movement
def partA(data) -> int:
    data = copy.deepcopy(data)
    done = False
    a = 0
    while True:
        sand_pos = Point(500 - K, 0)
        while True:
            if data[sand_pos.y + 1][sand_pos.x] != '.' and data[sand_pos.y + 1][sand_pos.x + 1] != '.' and data[sand_pos.y + 1][sand_pos.x - 1] != '.':
                break

            # straight
            if data[sand_pos.y + 1][sand_pos.x] == '.':
                obstacle = find_first(data, sand_pos)
                if obstacle == -1:
                    done = True
                    break
                data[sand_pos.y][sand_pos.x] = '.'
                sand_pos = Point(sand_pos.x, obstacle - 1)
                data[sand_pos.y][sand_pos.x] = 'o'
                continue

            # left
            if data[sand_pos.y + 1][sand_pos.x-1] == '.':
                test_pos = Point(sand_pos.x - 1, sand_pos.y)
                obstacle = find_first(data, test_pos)
                if obstacle == -1:
                    done = True
                    break
                data[sand_pos.y][sand_pos.x] = '.'
                sand_pos = Point(sand_pos.x-1, obstacle - 1)
                data[sand_pos.y][sand_pos.x] = 'o'
                continue

            #right
            if data[sand_pos.y + 1][sand_pos.x+1] == '.':
                test_pos = Point(sand_pos.x + 1, sand_pos.y)
                obstacle = find_first(data, test_pos)
                if obstacle == -1:
                    done = True
                    break
                data[sand_pos.y][sand_pos.x] = '.'
                sand_pos = Point(sand_pos.x+1, obstacle - 1)
                data[sand_pos.y][sand_pos.x] = 'o'
                continue
            break

        #for line in data:
            #print(*line)

        if done:
            break

        a += 1
    return a 


def partB(data):
    data[-1] = ['#'] * len(data[0])
    done = False
    a = 0
    while True:
        sand_pos = Point(500 - K, 0)
        while True:
            if data[sand_pos.y + 1][sand_pos.x] != '.' and data[sand_pos.y + 1][sand_pos.x + 1] != '.' and data[sand_pos.y + 1][sand_pos.x - 1] != '.':
                break

            # straight
            if data[sand_pos.y + 1][sand_pos.x] == '.':
                obstacle = find_first(data, sand_pos)
                if obstacle == -1:
                    done = True
                    break
                data[sand_pos.y][sand_pos.x] = '.'
                sand_pos = Point(sand_pos.x, obstacle - 1)
                data[sand_pos.y][sand_pos.x] = 'o'
                continue

            # left
            if data[sand_pos.y + 1][sand_pos.x-1] == '.':
                test_pos = Point(sand_pos.x - 1, sand_pos.y)
                obstacle = find_first(data, test_pos)
                if obstacle == -1:
                    done = True
                    break
                data[sand_pos.y][sand_pos.x] = '.'
                sand_pos = Point(sand_pos.x-1, obstacle - 1)
                data[sand_pos.y][sand_pos.x] = 'o'
                continue

            #right
            if data[sand_pos.y + 1][sand_pos.x+1] == '.':
                test_pos = Point(sand_pos.x + 1, sand_pos.y)
                obstacle = find_first(data, test_pos)
                if obstacle == -1:
                    done = True
                    break
                data[sand_pos.y][sand_pos.x] = '.'
                sand_pos = Point(sand_pos.x+1, obstacle - 1)
                data[sand_pos.y][sand_pos.x] = 'o'
                continue
            break

        #for line in data:
            #print(*line)

        a += 1
        if sand_pos.y == 0:
            break

    return a 


# So I want a set for each column, without knowing how much columns are there
# I can simply create sets with a buffer and then just trim sets on both sides
# now, either x will be different or y, and based on that I just want to walk through that difference and add it to my sets
def parse_data(data):
    matrix = [['.'] * N for _ in range(M)]
    highest_y = 0
    for line in data:
        line = line.split(' -> ')
        for i in range(1, len(line)):
            start, end = line[i - 1], line[i]
            start = Point(*map(int, start.split(',')))
            end = Point(*map(int, end.split(',')))
            highest_y = max(start.y, end.y, highest_y)
            start.x -= K
            end.x -= K
            if start.x != end.x:
                while start.x < end.x:
                    matrix[start.y][start.x] = '#'
                    start.x += 1
                while start.x > end.x:
                    matrix[start.y][start.x] = '#'
                    start.x -= 1

            elif start.y != end.y:
                while start.y < end.y:
                    matrix[start.y][start.x] = '#'
                    start.y += 1
                while start.y > end.y:
                    matrix[start.y][start.x] = '#'
                    start.y -= 1
            matrix[start.y][start.x] = '#'

    #cols = list(map(list, map(reversed, map(sorted, columns))))
    #for line in matrix:
        #print(*line)
    return matrix


data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
