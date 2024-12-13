from collections import defaultdict
from pprint import pprint
import sys
import heapq
from operator import add, concat, mul

from tqdm import tqdm

try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'

inp = open(FILE).read().splitlines()

def evaluate(res, nums, operators):
    heap = defaultdict(list)
    heap[0].append(nums[0])
    for i, num in enumerate(nums[1:]):
        for e in heap[i]:
            for op in operators: 
                heap[i+1].append(op(e, num))
    return any(e == res for e in heap[len(nums) - 1])

def concat_ints(a, b):
    return int(concat(str(a), str(b)))


def part1(inp):
    ans = 0
    operators = (add, mul)
    for line in inp:
        res, nums = line.split(':')
        nums = list(map(int, nums.split()))
        res = int(res)
        if evaluate(res, nums, operators):
            ans += res
    return ans 

def part2(inp):
    ans = 0
    operators = (add, mul, concat_ints)
    for line in tqdm(inp):
        res, nums = line.split(':')
        nums = list(map(int, nums.split()))
        res = int(res)
        if evaluate(res, nums, operators):
            ans += res
    return ans 
                    



        

print('Part1:', part1(inp))
print('Part2:', part2(inp))

