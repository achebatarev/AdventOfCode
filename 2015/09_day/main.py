import sys
from pprint import pprint
from collections import defaultdict
from aoc.lib import read_data
import heapq

try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'

def dijkstra(graph, node, size):
    #pprint(graph)
    pq = [(0, node, set([node]))]
    while pq:
        distance, node, visited = heapq.heappop(pq)
        if len(visited) == size:
            return distance
        for child, x in graph[node]:
            if child not in visited:
                v = visited.copy()
                v.add(child)
                heapq.heappush(pq, (distance + x, child, v))

    
        
        
        
def first(data):
    ans = float('inf') 
    for city in data:
        ans = min(ans, dijkstra(data, city, len(data)))
        #print(city)
    return ans
# just need to modify all distance to negative
def second(data):
    ans = 0
    for city in data:
        pass

def parse_data(data):
    graph = defaultdict(list) 
    for line in data:
        a, _, b, _, distance = line.split()
        graph[a].append((b, int(distance)))
        graph[b].append((a, int(distance)))
    #print(len(graph))
    return graph
    

data = read_data(FILE)
parsed_data = parse_data(data)
print(first(parsed_data))
print(second(parsed_data))
