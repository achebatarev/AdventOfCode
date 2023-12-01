import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq

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


def partA(data):
    q = deque([20, 60, 100, 140, 180, 220])
    result = []
    x = 1
    cycle = 0
    for e in data:
        if e.startswith('addx'):
            _, val = e.split()
            if q and cycle + 2 >= q[0]:
                result.append(x * q.popleft())
            x += int(val)
            cycle += 2
        else:
            cycle += 1

        if q and cycle == q[0]:
            result.append(x * q.popleft())

    return sum(result)

    pass


def partB(data):
    arr = [['.'] * 40 for _ in range(6)]
    q = deque(data)
    second = False
    n = 1
    for i in range(6):
        for j in range(40):
            #print('Sprite', n, 'loc', i)
            if j >= (n - 1) and j <= (n + 1):
                #print(i)
                arr[i][j] = '#'

            if q[0].startswith('addx'):
                if second:
                    _, val = q.popleft().split()
                    n += int(val)
                    second = False
                else:
                    second = True
            else:
                q.popleft()

    for line in arr:
        print(*line)


def parse_data(data):
    return data


data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
