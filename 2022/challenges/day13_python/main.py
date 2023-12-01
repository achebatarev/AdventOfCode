import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
import json
from functools import total_ordering

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'


def read_data(filename: str):
    data = []
    with open(filename, 'r') as f:
        return f.read().split('\n\n')


def cmp(a, b):
    return compare_lists(a, b)


@total_ordering
class Beast:

    def __init__(self, val):
        self.l = val

    def __eq__(self, other):
        return compare_lists(self.l, other.l) == 0

    def __lt__(self, other):
        return compare_lists(self.l, other.l) == 1


# both integers
#both lists
# one list, one integer
# one empty, one has item
# if smaller
def compare_lists(list1, list2) -> int:
    for e1, e2 in zip(list1, list2):
        if type(e1).__name__ == 'int' and type(e2).__name__ == 'int':
            if e1 > e2:
                return -1
            elif e1 == e2:
                continue
            else:
                return 1
        elif type(e1).__name__ == 'int' and type(e2).__name__ == 'list':
            res = compare_lists([e1], e2)
            if res == 0:
                continue
            elif res == 1:
                return 1
            else:
                return -1

        elif type(e1).__name__ == 'list' and type(e2).__name__ == 'int':
            res = compare_lists(e1, [e2])
            if res == 0:
                continue
            elif res == 1:
                return 1
            else:
                return -1
        else:
            res = compare_lists(e1, e2)
            if res == 0:
                continue
            elif res == 1:
                return 1
            else:
                return -1

    if len(list1) > len(list2):
        return -1
    elif len(list1) < len(list2):
        return 1
    else:
        return 0


def partA(data):
    result = []
    for i, pair in enumerate(data):
        l1 = json.loads(pair.splitlines()[0])
        l2 = json.loads(pair.splitlines()[1])
        if compare_lists(l1, l2) == 1:
            result.append(i + 1)
    print(sum(result))
    return result


def partB(data):
    v1 = [[2]]
    v2 = [[6]]
    l = []
    l.append(Beast([[2]]))
    l.append(Beast([[6]]))
    for i, pair in enumerate(data):
        l1 = json.loads(pair.splitlines()[0])
        l2 = json.loads(pair.splitlines()[1])
        l.append((Beast(l1)))
        l.append((Beast(l2)))
    l.sort()
    res = 1
    for i, e in enumerate(l):
        if e.l == v1:
            res *= (i + 1)
        if e.l == v2:
            res *= (i + 1)
    return res


def parse_data(data):
    return data


data = read_data(FILE)
parsed_data = parse_data(data)
print(*partA(parsed_data), sep='\n')
#print(partB(parsed_data))
