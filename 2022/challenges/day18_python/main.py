import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
from dataclasses import dataclass
sys.setrecursionlimit(10**4)
try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'

moves = [(-1, 0, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1)]

@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int
    z: int

def read_data(filename: str):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data

def partA(data):
    ans = 0
    for p in data:
        res = 6 
        for r, c, u in moves:
            new = Point(p.x+r, p.y+c, p.z+u)
            if new in data:
                res -= 1
        ans += res
    return ans

def flood_fill(points, p, s, l, visited):
    if p in visited:
        #print('we been here boss')
        return 0
    if p in points:
        return 1
    if not (s.y <= p.y <= l.y and s.x <= p.x <= l.x and s.z <= p.z <= l.z):
        #print(p, 'out of bounds')
        return 0
    ans = 0 
    visited.add(p)
    #print(p)
    for r,c,u in moves:
        new = Point(p.x+c, p.y+r, p.z+u)
        ans += flood_fill(points, new, s, l, visited)
    return ans


# either expanding moves, or have to walk through until the last x, y, or z on that side
# I can find, largest and smallest x, y and z, and that will be my boundaries
# Do I need to count only exterior sides?
# I am getting blocked by too many cubes
# Double counting?
# anything that is in contact with outside, is the outside, no matter if it has something under or not
# I can simply try excluding from flood filling the points that has one of the x,y,z equal to max or min, but I am not sure if that will handle all of the case
# It will not
# what is the definition of element that are on the outer layer
# Each node side can be on inside our outside
# I can launch my flood fill algorithm on outside and it will give me all of the node that are on outside
# I also need to identify the starting point, as long as I do not start inside, nor on the point, oh, if I just start in one of the s or l pos -1, we should be good
def partB(data):
    #pprint(data)
    sy, ly = min(data, key=lambda x: x.y).y, max(data, key=lambda x: x.y).y
    sx, lx = min(data, key=lambda x: x.x).x, max(data, key=lambda x: x.x).x
    sz, lz = min(data, key=lambda x: x.z).z, max(data, key=lambda x: x.z).z
    s, l = Point(sx-1, sy-1, sz-1), Point(lx+1, ly+1, lz+1)
    start = Point(sx-1, sy-1, sz-1)
    return flood_fill(data, start, s, l, set())
    #print(sy, ly)
    #print(sx, lx)
    #print(sz, lz)
    #for p in data:
        #res = 6 
        #print('New Point', p)
        #for r, c, u in moves:
            #t = Point(p.x+c, p.y+r, p.z+u)
            #while sy <= t.y <= ly and sx <= t.x <= lx and sz <= t.z <= lz:
                #if t in data:
                    #print(t)
                    #res -= 1
                    #break
                #t = Point(t.x+c, t.y+r, t.z+u)
        #print(res)
        #ans += res
    #v = 7
    #print(sz <= v <= lz, v >= sz and v <= lz)
             



def parse_data(data):
    points = set() 
    for line in data:
        points.add(Point(*map(int,line.split(','))))
    return points 

data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
