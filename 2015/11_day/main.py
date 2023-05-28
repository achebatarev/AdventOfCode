import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
from aoc.lib import read_data

try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'

def read_data(filename: str):
    data = []
    with open(filename, 'r') as f:
        data = f.readline().strip()
    return data
# I should just count in base 26 and check the validity of the new password
def first(data):
    pass

def second(data):
    pass

def parse_data(data):
    print(data)
    return data

data = read_data(FILE)
parsed_data = parse_data(data)
print(first(parsed_data))
print(second(parsed_data))
