import sys
from typing import Callable
from pprint import pprint
from collections import defaultdict, deque, Counter
from dataclasses import dataclass
import heapq

try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'

@dataclass
class Reflection:
    position: int
    type_: str

def read_data(filename: str) -> str:
    with open(filename, 'r') as f:
        return f.read()

def walk_part1(arr: list[str], i: int, j: int) -> bool:
    while i >= 0 and j < len(arr):
        if arr[i] != arr[j]:
            return False
        i -= 1
        j += 1
    return True

def equal_with_smudge(line1: str, line2: str, smudge: list[bool]) -> bool:
    for e1, e2 in zip(line1, line2):
        if e1 != e2 and smudge[0]:
            smudge[0] = False
            continue
        elif e1 != e2:
            return False
    return True

def walk_part2(arr: list[str], i: int, j: int) -> bool:
    smudge = [True] 
    while i >= 0 and j < len(arr):
        if not equal_with_smudge(arr[i], arr[j], smudge):
            return False
        i -= 1
        j += 1
    return True

def find_reflection(arr: list[str], walk: Callable[[list[str], int, int], bool], reflection = -1) -> int:
    for i, _ in enumerate(arr[:-1]):

        if i != reflection and walk(arr, i, i+1):
            return i 
    return -1 
    #raise ValueError("Ran through entire pattern without finding any reflections")

def first(data: list[list[str]]) -> int:
    ans = 0
    for pattern in data:
        ans += (find_reflection(pattern, walk_part1) + 1) * 100
        ans += find_reflection(list(zip(*pattern)), walk_part1) + 1
    return ans

# assuming a pattern can have only one reflection
def find_reflections(pattern: list[str]) -> Reflection:
    res = find_reflection(pattern, walk_part1) 
    if res != -1:
        return Reflection(res, 'h')

    res = find_reflection(list(zip(*pattern)), walk_part1) 
    if res != -1:
        return Reflection(res, 'v')

    raise Exception("No reflection found")

def second(data):
    ans = 0
    for pattern in data:
        reflection = find_reflections(pattern)
        res = find_reflection(pattern, walk_part2, reflection.position if reflection.type_ == 'h' else -1)
        if res != -1:
            if reflection.type_ == 'h' and reflection.position == res:
                raise Exception("We're repeating the pattern")
            ans += (res+1) * 100
            continue

        res = find_reflection(list(zip(*pattern)), walk_part2, reflection.position if reflection.type_ == 'v' else -1)
        if res != -1:
            if reflection.type_ == 'v' and reflection.position == res:
                raise Exception("We're repeating the pattern")
            ans += (res+1)
            continue
        raise ValueError("No Pattern found, impossible!!!")
    return ans

def parse_data(data: str) -> list[list[str]]:
    return [e.splitlines() for e in data.split('\n\n')]

if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(first(parsed_data))
    print(second(parsed_data))
