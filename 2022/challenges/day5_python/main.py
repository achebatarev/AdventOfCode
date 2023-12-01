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
class Instruction: 
    amount: int
    start: int
    dest: int

def read_data(filename: str):
    with open(filename, 'r') as f:
        crates, instructions = f.read().split('\n\n')
    return (crates.splitlines(), instructions.splitlines()) 

def first(data):
    crates, instructions = data 
    crates = [crate.copy() for crate in crates]
    for inst in instructions:
        for _ in range(inst.amount):
            crates[inst.dest].append(crates[inst.start].pop())
    result = [] 
    for stack in crates:
        if stack:
            result.append(stack.pop())
    return ''.join(result)

def second(data):
    crates, instructions = data[:]
    for inst in instructions:
        new_crates = []
        for _ in range(inst.amount):
            new_crates.append(crates[inst.start].pop())
        crates[inst.dest].extend(new_crates[::-1])
    result = [] 
    for stack in crates:
        if stack:
            result.append(stack.pop())
    return ''.join(result)

def parse_data(data):
    crates, instructions = data
    parsed_crates = [deque() for _ in range(len(crates[-1].split()))] 
    parsed_instructions = []
    for line in crates[::-1][1:]:
        line = list(line) 
        c = 0 
        for i in range(1, len(line), 4):
            char = line[i]
            if char.isalnum():
                parsed_crates[c].append(char)
            c += 1
    for instruction in instructions:
        t = instruction.split()
        parsed_instructions.append(Instruction(int(t[1]), int(t[3]) -1, int(t[5]) -1))

    return (parsed_crates, parsed_instructions)

data = read_data(FILE)
parsed_data = parse_data(data)
print(first(parsed_data))
print(second(parsed_data))
