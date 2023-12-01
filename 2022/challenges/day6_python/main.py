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
        return f.read().strip()

def first(data):
    for i in range(0, len(data)-4):
        if len(set((data[i], data[i+1], data[i+2], data[i+3]))) == 4:
            return i + 4

def second(data):
    return [i + 14 for i in range(0, len(data)-14) if len(set(data[i:i+14])) == 14][0]
        

def parse_data(data):
    return data

data = read_data(FILE)
parsed_data = parse_data(data)
#print(parsed_data)
print(first(parsed_data))
print(second(parsed_data))
