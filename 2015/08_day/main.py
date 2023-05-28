import sys
from pprint import pprint
from aoc.lib import read_data
import ctypes

try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'

def second(data):
    total = 0
    total_c = 0
    for s in data:
        total_c += 2 + len(s)
        total += len(s)
        for l in s:
            if l in ('\\', '"'):
                total_c += 1
    print(total_c - total)


def first(data):
    ans = []
    total = 0
    total_c = 0
    for s in data:
        total += len(s)
        i = 0
        c = 0
        while i < len(s):
            if s[i] == '\\' and s[i+1] == 'x':
                i += 4
                total_c += 1
            elif s[i] == '\\':
                i += 2
                total_c += 1
            elif s[i] != "\"":
                c += 1
                total_c += 1
                i += 1
            else:
                i += 1
    print(total - total_c)

    return ans 

data = read_data(FILE)
first(data)
second(data)