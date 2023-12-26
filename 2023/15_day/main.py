import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
from dataclasses import dataclass
import heapq
from functools import cache

try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'


def read_data(filename: str) -> str:
    with open(filename, 'r') as f:
        return f.read()
    
@dataclass
class Lens:
    label: str
    focal_length: int = 0



@cache
def hash_(string: str, current_value: int = 0) -> int:
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

def first(data) -> int:
    return sum(hash_(e) for e in data)

class HashMap:
    def __init__(self, size=256):
        self.d = [[] for _ in range(size)]
        self.values = {}

    def insert(self, label: str, value: int):
        key = hash_(label)
        self.values[label] = value
        if label not in self.d[key]:
            self.d[key].append(label)

    def remove(self, label: str):
        key = hash_(label)
        if label in self.d[key]:
            self.d[key].remove(label)

    def calculate(self) -> int:
        ans = 0
        for i, box in enumerate(self.d):
            for j, label in enumerate(box):
                ans += (i+1) * (j+1) * self.values[label]

        return ans




def second(data: list[str]) -> int:
    hashmap = HashMap(256) 
    for e in data:
        if '=' in e:
            label, value = e.split('=')
            hashmap.insert(label, int(value))
        if '-' in e: 
            hashmap.remove(e[:-1])


    return hashmap.calculate()

def parse_data(data):
    return data.strip().split(',') 

if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(first(parsed_data))
    print(second(parsed_data))
