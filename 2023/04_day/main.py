from operator import mul
import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
from dataclasses import dataclass
import heapq

try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'

@dataclass
class Scratchcard:
    n: int
    winning: set[int]
    you: set[int]

def read_data(filename: str):
    with open(filename, 'r') as f:
        return f.read().splitlines()

def first(data):
    ans = 0
    for card in data:
        multiplier = 1
        for n in card.you:
            if n in card.winning:
                multiplier *= 2
        ans += multiplier//2
    return ans
                

def second(data):
    l = [1] * len(data)
    for i, card in enumerate(data):
        mult = 1
        for n in card.you:
            if n in card.winning:
                if i+mult >= len(data):
                    break 
                l[i+mult] += l[i]
                mult += 1
                
    return sum(l)

def parse_data(data):
    l = []
    for line in data:
        card, numbers = line.split(':')
        n = int(card.split()[1])
        winning, you = numbers.split('|')
        
        l.append(Scratchcard(n, set(map(int, winning.split())), set(map(int, you.split()))))

    
    return l 

if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(first(parsed_data))
    print(second(parsed_data))
