import sys

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'

grid = list(map(list, open(FILE).read().splitlines()))
grid = [list(map(int, line)) for line in grid]
mapping = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def dfs(grid, y, x, prev, visited):
    # print(len(grid), len(grid[0]))
    # print(y, x)
    if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and (grid[y][x] - prev == 1):
        if grid[y][x] == 9:
            # if (y, x) in visited:
            #     return 0
            # visited.add((y, x))
            return 1
        a = 0
        for r, c in mapping:
            yr = y+r
            xc = x+c
            a += dfs(grid, yr, xc, grid[y][x], visited)
        return a

    return 0

ans = 0
for i, line in enumerate(grid):
    for j, e in enumerate(line):
        if e == 0:
            visited = set()
            ans += dfs(grid, i, j, -1, visited)
print('PART 1:', ans)
