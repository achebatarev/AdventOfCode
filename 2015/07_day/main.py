import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
from aoc.lib import read_data
# this seems like a topological sorting problem exactly like in CCSC
try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'

mask = 0xFFFF
graph = defaultdict(list)
indegree = defaultdict(int)
values = {}
ops = {}
start = deque()

def evaluate(x):
    global ops, values
    op, a, b = ops[x]
    if a and not a.isdigit():
        a = values[a]
    if b and not b.isdigit():
        b = values[b]
    if a: 
        a = int(a)
    if b:
        b = int(b)
    if op == 'AND':
        return (a & b) 
    if op == 'LSHIFT':
        return (a << b)
    if op == 'OR':
        return (a | b) 
    if op == 'RSHIFT':
        return (a >> b) 
    if op == 'NOT':
        return (~a & mask)
    if op == 'AS':
        return (a) 


def parse(a, b, op=False):
    global graph, indegree, values
    if a.isdigit():
        if op:
            values[b] = a
    else:
        indegree[b] += 1
        graph[a].append(b)

# need to create a graph, indegree, operations for each register
def parse_data(data):
    global graph, indegree, values, ops, start
    for line in data:
        t = line.split()
        if any(op in t for op in ('RSHIFT', 'OR', 'AND', 'LSHIFT')):
            a, op, b, _, c = t
            parse(a, c)
            parse(b, c)
            ops[c] = (op, a, b)
        elif 'NOT' in t:
            op, a, _, b = t
            parse(a, b, True)
            ops[b] = (op, a, None)
        else:
            a, _, b = t
            parse(a, b, True)
            ops[b] = ('AS', a, None)
        if indegree[t[-1]] == 0:
            start.append(t[-1])
    return data 

def traverse():
    global graph, indegree, values, ops, start
    while start:
        node = start.popleft()
        values[node] = evaluate(node)
        for child in graph[node]:
            indegree[child] -= 1
            if indegree[child] <= 0:
                start.append(child)

data = parse_data(read_data(FILE))
#print(indegree)
#pprint(indegree)
#pprint(values)
traverse()
print(values)

