import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
from dataclasses import dataclass
import heapq

try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'


def read_data(filename: str):
    with open(filename, 'r') as f:
        return f.read().splitlines()

def first(data):
    return data

def second(data):
    return data

def parse_data(data):
    return data 

data = read_data(FILE)
parsed_data = parse_data(data)
print(first(parsed_data))
print(second(parsed_data))
