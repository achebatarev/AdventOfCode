import sys
from copy import deepcopy
import heapq as hq
from pprint import pprint
from collections import deque
# speed up dijkstra or switch to a*
def first(arr):
    visited = set() 
    unvisited = [] 
    weights = {}
    for i, line in enumerate(arr):
        for j, e in enumerate(line):
            weights[(j, i)] = sys.maxsize
            unvisited.append((j, i))
    weights[(0, 0)] = 0
    check = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    prev = {}

    while unvisited:
        #(o(n))
        current_node = min(unvisited, key=lambda x: weights[x])  
        #weight = weights[current_node]
        for i, j in check:
            xj = current_node[0] + j
            yi = current_node[1] + i
            if xj >= 0 and xj < len(arr[0]) and yi >= 0 and yi < len(arr):
                neighbour = (xj, yi)
                neighbour_weight = weights[current_node] + arr[yi][xj]
                if neighbour_weight < weights[neighbour]:
                    weights[neighbour] = neighbour_weight
                    prev[neighbour] = current_node
        #(o(n))
        unvisited.pop(unvisited.index(current_node))
        visited.add(current_node)

    return weights[(len(arr[0])-1, len(arr)-1)]

def second(arr):
    queue = []
    visited = set()
    hq.heappush(queue, (0, (0, 0)))
    weights = {}
    for i, line in enumerate(arr):
        for j, e in enumerate(line):
            weights[(j, i)] = sys.maxsize
    weights[(0, 0)] = 0
    while queue:
        weight, current_node = hq.heappop(queue)
        visited.add(current_node)
        check = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i, j in check:
            xj = current_node[0] + j
            yi = current_node[1] + i
            if xj >= 0 and xj < len(arr[0]) and yi >= 0 and yi < len(arr) and (xj, yi) not in visited:
                neighbour = (xj, yi)
                neighbour_weight = weights[current_node] + arr[yi][xj]
                if neighbour_weight < weights[neighbour]:
                    weights[neighbour] = neighbour_weight
                    hq.heappush(queue, (neighbour_weight, neighbour))
    return weights[(len(arr[0])-1, len(arr)-1)]





def generate_full_map(arr):
    new_arr = deepcopy(arr)
    for k in range(1,5):
        for line in arr:
            new_line = []
            for e in line:
                new_line.append(e+k if e+k<=9 else (e+k) - 9)
            new_arr.append(new_line)
    true_arr = deepcopy(new_arr)
    for k in range(1, 5):
        for i, line in enumerate(new_arr):
            l = [] 
            for e in line:
                l.append(e+k if e+k <= 9 else (e+k)-9)
            true_arr[i].extend(l)
    return true_arr
                    


arr = []
with open('input') as f:
    for line in f.readlines():
        arr.append(list(map(int, line.strip())))

print(first(arr))
new_arr = generate_full_map(arr)
print(second(new_arr))
