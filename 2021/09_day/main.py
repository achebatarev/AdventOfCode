from pprint import pprint
from functools import reduce
from copy import deepcopy
def first(inp):
    r = 0
    check = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i, line in enumerate(inp):
        for j,e in enumerate(line):
            for x, y in check:
                try:
                    if inp[i+x][j+y] <= e:
                        break
                except:
                    pass
            else:
                r += int(e) +1
    return r

def second(inp):
    l = []
    # find all low points, emunrate through them
    lowest = []
    for i, line in enumerate(inp):
        for j, e in enumerate(line):

            check = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for x, y in check:
                try:
                    if inp[i+x][j+y] <= e:
                        break
                except:
                    pass
            else:
                lowest.append((j, i))
    for j, i in lowest:
        l.append(find_basin(inp, j, i, -1))
    return reduce(lambda x, y: x*y, sorted(l)[-3:])


def find_basin(inp, x, y, prev):
    if (x < 0 or x >= len(inp[0]) or y < 0 or y >= len(inp)):
        return 0
    elif inp[y][x] == -1:
        return 0 
    elif inp[y][x] == 9 or prev >= inp[y][x]:
        return 0
    r = 1
    curr = inp[y][x]
    inp[y][x] = -1
    check = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i,j in check:
        xi = x + i
        yj = y + j
        if curr != 9:
            found = find_basin(inp, x+i, y+j, curr)
            r += found
    return r

with open('input', 'r') as f:
    l = []
    for line in f.readlines():
        l.append(list(map(int,line.strip())))

print(first(l))
print(second(l))
