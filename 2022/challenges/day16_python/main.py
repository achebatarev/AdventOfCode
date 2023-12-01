import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
import re
import time

total = 0

try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'

def read_data(filename: str):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data

def calculate_dist(graph, root):
    global valve
    q = deque([root])
    d = {}
    level = 1
    visited = set()
    visited.add(root)
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node != root and valve[node] != 0: 
                d[node] = level

            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    q.append(child)
        level += 1
    return d 

def set_bit(n, k) -> int:
    return n | (1 << k)

def get_bit(n, k) -> int:
    return n & (1 << k)
# I am traversing the wieghted graph, where each weight, represents, how long it will take to open the valve
# openning the valve will give me certain gain
# With a small enough input, where we can open every valve, the problem becomes
# find a path that will give maximum yield vising each vertex only once
#def dpA(graph, node, k, opened) -> int:
    #global total, valve
    #if  opened == total:
        #return 0
    #if k < 0:
        #return 0
    ##if node in memo and k in memo[node]:
        ##return memo[node][k]
    #r = 0 
    #for child, dist in graph[node]:
        #if not get_bit(opened, indecis[child]) and k-dist >= 0:
            #r = max(dpA(graph, child, k-dist, set_bit(opened, indecis[child])) + valve[node]*k, r)

    #return r

#def recursive_dp(distances, k):
    #global total, indecis
    #graph = dict([(key, list(item.items())) for key, item in distances.items()])
    ## TODO calculate total number of valves that can be opened
    #total = 0
    #indecis = {}
    #for node in graph:
        #if valve[node] != 0:
            #indecis[node] = total
            #total += 1
    #total = (2 ** total) - 1

    #return dpA(graph, 'AA', k, 0)
    
def iterative(distances, k) -> int:
    global valve, memo, total
    graph = dict([(key, list(item.items())) for key, item in distances.items()])
    #pprint(graph)
    q = deque([('AA', 1, 0, 0)])
    total = 0
    indecis = {}
    for node in graph:
        if valve[node] != 0:
            indecis[node] = total
            total += 1
    ans = 0
    memo = defaultdict(int) 
    while q:
        #q = deque(sorted(list(q), key=lambda x: x[-1], reverse=True))
        for _ in range(len(q)):
            node, move, opened, score = q.popleft()
            #if score >= ans:
                #print(score)
                #for i in range(total):
                    #if get_bit(opened, i):
                        #print([k for k, v in indecis.items() if v == i])
            ans = max(ans, score) 
            for child, dist in graph[node]:
                if not get_bit(opened, indecis[child]) and move+dist <= k:
                    new_score = score+valve[child]*(k - (move+dist)+1)
                    o = set_bit(opened, indecis[child])
                    #if new_score == 762: 
                        #print('What the fuck')
                        #for i in range(total):
                            #if get_bit(opened, i):
                                #print([k for k, v in indecis.items() if v == i])
                    if o in memo and new_score < memo[o]:
                        continue
                    memo[o] = new_score
                    if new_score == 762: 
                        print(new_score)
                        for i in range(total):
                            if get_bit(opened, i):
                                print([k for k, v in indecis.items() if v == i])
                    q.append((child, move+dist, o, new_score))
    return ans



def partA(data):
    k = 30
    distances = {}
    for node in data:
        distances[node] = calculate_dist(data, node)
    return iterative(distances, k)

# shared opened array, but now I have two actors
# since I am only accounting for how long it takes me to get to point B, that might be problematic, since, another actor might be doing nothing
# What if we make one actor to go to A and another actor go to B, and then just skip to the point of the minimum of A and B
# I think I can do the same idea I done with the dfs, but just do it in the bfs form
#Goal: optimize runtime
# Right now:
# I keep both elephant and me in the same object
# I move either elephant or me certain distance
# I can actually memoize paths !!!!! I just need to represent them as an integer 
def partB_old(data):
    k = 26
    distances = {}
    for node in data:
        distances[node] = calculate_dist(data, node)
    graph = dict([(key, list(item.items())) for key, item in distances.items()])
    ans = 0
    q = deque([('AA', 'AA', 1, 1, 0, 0, 0)])

    total = 0
    indecis = {}
    for node in graph:
        if valve[node] != 0:
            indecis[node] = total
            total += 1
    total = (2 ** total) - 1

    while q:
        q = deque(sorted(list(q), key=lambda x: x[-2], reverse=True)[:1000000])
        for _ in range(len(q)):
            nodeA, nodeB, moveA, moveB, scoreA, scoreB, opened = q.popleft()
            score = scoreA + scoreB
            if score > ans:
                if scoreA == 764 or scoreB == 764:
                    for i in range(total):
                        if get_bit(opened, i):
                           print([k for k, v in indecis.items() if v == i])
                print(scoreA, scoreB, score)
            #if score > ans:
                #print(score, moveA, moveB, f'{bin(opened)}/{bin((2**total) - 1)}')
            ans = max(ans, score)
            if moveA < moveB:
                for child, dist in graph[nodeA]:
                    if not get_bit(opened, indecis[child]) and moveA+dist <= k:
                        q.append((child, nodeB, moveA+dist, moveB, scoreA+valve[child]*(k - (moveA+dist)+1), scoreB, set_bit(opened, indecis[child])))

            else:
                for child, dist in graph[nodeB]:
                    if not get_bit(opened, indecis[child]) and moveA+dist <= k:
                        q.append((nodeA, child, moveA, moveB+dist, scoreA, scoreB+valve[child]*(k - (moveB+dist)+1), set_bit(opened, indecis[child])))
    return ans

def count_bits(n):
    i = 0
    while n:
        n = n & (n-1)
        i += 1
    return i

def dfs(group, values, n, level, memo):
    global mask 
    res = 0
    if n in values:
        return values[n]
    if n in memo:
        return memo[n]
    for k in group[level]:
        if ~n & mask & k != 0:
            continue
        res = max(dfs(group, values, level-1, k, memo), res)
    memo[n] = res 
    return memo[n]

    

# I need mask of size number of element
# elephant does nto have to open all of the complement valves, it can open any number of them 
# If I know the best score if we can only open those valves, it is very easy to solve
# More valves I open, more value I will get
def partB(data):
    global memo, total, mask
    starting = time.time()
    memo = {}
    k = 26
    distances = {}
    for node in data:
        distances[node] = calculate_dist(data, node)
    iterative(distances, k)
    mask = int('1' * total, 2)
    res = 0 
    #group = defaultdict(list) 
    #for n in memo:
        #group[count_bits(n)].append(n)
    ##dfs(group, memo, total, me)
    #pprint(group)
    #for i in range(536854528):
        #pass
    tried = set()
    for n in memo:
        flip = ~n & mask 
        #print(bin(flip))
        #for k, v in memo.items():
            #t = flip & k
            #if t != 0:
                #print(t, bin(flip), bin(k), v)
        if n not in memo:
            continue
        try:
            b = iter(v for k,v in memo.items() if n & k == 0)
            b = max(b)

        except:
            continue
        #print('{0:016b}'.format(n), '{0:016b}'.format(flip), total)
        #print('{0:015b}'.format(n), n, '{0:015b}'.format(flip), flip, total)
        a = b + memo[n]
        #if a >= res:
            #print(a, b, memo[n])
        res = max(a, res)
    print(time.time() - starting)
    return res

def parse_data(data):
    global valve
    valve = {}
    graph = defaultdict(list)
    for line in data:
        nodes = re.findall('[A-Z]{2}', line)
        val = int(re.findall(r'\d+', line)[0])
        root = nodes[0]
        valve[root] = val 
        graph[root].extend(nodes[1:])
    return graph 

if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(partA(parsed_data))
    print(partB(parsed_data))