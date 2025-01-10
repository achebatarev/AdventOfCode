import sys

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'

G = { y+x*1j: e
        for y, l in enumerate(open(FILE).read().splitlines())
        for x, e in enumerate(l)
        }

def dfs(g, p, visited):
    if p in visited:
        return 0, 0
    visited.add(p)
    nps = [p+d for d in [1, -1, 1j, -1j] if g.get(p+d, '') == g[p]]
    a, per = 1, 4 - len(nps)
    for np in nps:
        area, perimeter = dfs(g, np, visited)
        a += area
        per += perimeter 
    return a, per

# TODO: 
# 1. Find all of the perimeters
# 2. Find consecutive sequences and condense them

v = set()
ans = 0
for e in G:
    a, p = dfs(G, e, v)
    ans += a * p

print("PART 1:", ans)



