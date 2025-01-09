import sys

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'

G = { y+x*1j: int(e)
        for y, line in enumerate(open(FILE).read().splitlines())
        for x, e in enumerate(line)
    }

def dfs(g, p):
    if g[p] == 9:
        return 1
    ans = 0
    for e in (p+d for d in [1, -1, 1j, -1j] if g.get(p+d) == g[p] + 1):
        ans += dfs(g, e)
    return ans

ans = sum(dfs(G, p) for p in G if G[p] == 0)
        
print('PART 2:', ans)
