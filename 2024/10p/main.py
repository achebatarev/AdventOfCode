import sys

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'


grid = list(map(list, open(FILE).read().splitlines()))
grid = [list(map(int, line)) for line in grid]
G = {y+x*1j: c
     for y, l in enumerate(open(FILE).read().splitlines())
     for x, c in enumerate(map(int, l))}
mapping = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def gaussian_dfs(grid, p, prev):
    if p not in G or grid[p] - prev != 1:
        return 0
    if grid[p] == 9:
        return 1
    return sum(gaussian_dfs(grid, p+r+c*1j, grid[p]) for r, c in mapping)

ans = sum(gaussian_dfs(G, k, -1) for k in G)
        
print('PART 2:', ans)
