import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import itertools
import heapq
from aoc.lib import read_data

try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'

def play(s):
    ans = []
    for e, group  in itertools.groupby(s):
        group = list(group)
        ans.extend([str(len(group))] + [e])
    #print(ans)
    return ''.join(ans)

def first(s):
    for _ in range(50):
        s = play(s)
    return len(s)

def second(data):
    pass

def parse_data(data):
    pass

#data = read_data(FILE)
#parsed_data = parse_data(data)
parsed_data = '1113222113'
print(first(parsed_data))
print(second(parsed_data))
