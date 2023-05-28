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
from typing import Optional
from enum import Enum

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'

@dataclass
class Instruction:
    type: str
    a: str
    b: Optional[str] = None

class Type(Enum):
    set = 'set'
    snd = 'snd'
    add = 'add'
    mul = 'mul'
    mod = 'mod'
    rcv = 'rcv'
    jgz = 'jgz'



def read_data(filename: str):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data

# b can be a variable or int
def partA(data):
    freq = 0
    ans = 0
    d = defaultdict(int) 
    i = 0
    while i < len(data):
        instruction = data[i] 
        bval = 0
        if instruction.b:
            if instruction.b.lstrip('-').isdigit():
                bval = int(instruction.b)
            else:
                bval = d[instruction.b]
        addd = 1
        if instruction.type == Type.set.value:
            d[instruction.a] = bval 
        elif instruction.type == Type.snd.value:
            freq = d[instruction.a]
        elif instruction.type == Type.add.value:
            d[instruction.a] += bval 
        elif instruction.type == Type.mul.value:
            d[instruction.a] *= bval 
        elif instruction.type == Type.mod.value:
            d[instruction.a] %= bval 
        elif instruction.type == Type.rcv.value:
            if freq != 0:
                ans = freq
                break
        elif instruction.type == Type.jgz.value:
            if d[instruction.a] > 0:
                addd = bval 
        else:
            raise Exception('Why?')
        i += addd
    return ans    

def worker(id, recv, send, data):
    d = defaultdict(int) 
    ans = 0
    d['p'] = id
    i = 0
    while i < len(data):
        instruction = data[i] 
        bval = 0
        if instruction.b:
            if instruction.b.lstrip('-').isdigit():
                bval = int(instruction.b)
            else:
                bval = d[instruction.b]

        addd = 1
        if instruction.type == Type.set.value:
            d[instruction.a] = bval 
        elif instruction.type == Type.snd.value:
            ans += 1
            n = 0
            if instruction.a.lstrip('-').isdigit():
                n = int(instruction.a)
            else:
                n = d[instruction.a]
            send.append(n)
        elif instruction.type == Type.add.value:
            d[instruction.a] += bval 
        elif instruction.type == Type.mul.value:
            d[instruction.a] *= bval 
        elif instruction.type == Type.mod.value:
            d[instruction.a] %= bval 
        elif instruction.type == Type.rcv.value:
            if recv:
                d[instruction.a] = recv.popleft()
            else:
                yield ans
                continue
        elif instruction.type == Type.jgz.value:
            if instruction.a.isdigit() or d[instruction.a] > 0:
                addd = bval 
        else:
            raise Exception('Why?')
        i += addd
    return ans


def brute_force(data):
    ans = 0
    first = True
    firstQueue, secondQueue = deque(), deque()
    worker1, worker2 = worker(0, firstQueue, secondQueue, data), worker(1, secondQueue, firstQueue, data)
    while firstQueue or secondQueue or first:
        next(worker1)
        ans = next(worker2)
        first = False
    return ans

def stupid(data):
    q = deque()
    ans = 0
    d1 = defaultdict(int) 
    d2 = defaultdict(int)
    i = 0
    while i < len(data):
        instruction = data[i] 
        bval = 0
        if instruction.b:
            if instruction.b.lstrip('-').isdigit():
                bval = int(instruction.b)
            else:
                bval = d1[instruction.b]
        addd = 1
        if instruction.type == Type.set.value:
            d1[instruction.a] = bval 
        elif instruction.type == Type.snd.value:
            ans += 1
            q.append((d2[instruction.a], d1[instruction.a]))
        elif instruction.type == Type.add.value:
            d1[instruction.a] += bval 
            d2[instruction.a] += bval 
        elif instruction.type == Type.mul.value:
            d1[instruction.a] *= bval 
            d2[instruction.a] *= bval 
        elif instruction.type == Type.mod.value:
            d1[instruction.a] %= bval 
            d2[instruction.a] %= bval 
        elif instruction.type == Type.rcv.value:
            if not q:
                break
            d1[instruction.a], d2[instruction.a] = q.popleft()
        elif instruction.type == Type.jgz.value:
            if instruction.a.isdigit() or d1[instruction.a] > 0:
                addd = bval 
        else:
            raise Exception('Why?')
        i += addd
    return ans    


def partB(data):
    return brute_force(data)

def parse_data(data):
    ans = []
    for line in data:
        ans.append(Instruction(*line.split()))
    return ans
        


if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(partA(parsed_data))
    print(partB(parsed_data))
