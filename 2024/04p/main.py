letters = {'X': 'M', 'M': 'A', "A": "S"}
mapping = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1))
def dfs(arr, y, x, count):
    res = 0
    for r, c in mapping:
        yr = y
        xc = x
        l = []
        locs = []
        for _ in range(4):
            if 0 <= yr < len(arr) and 0 <= xc < len(arr[0]):
                l.append(arr[yr][xc])
                # locs.append((yr, xc))
            # because of this lazy handling, some values become negative and wrap around
            yr = yr+r
            xc = xc+c
        if ''.join(l) == 'XMAS':
            res += 1
            # print(count, locs, l)
            count+=1
    return res, count



# f = open('input.d4')
f = open('input.d4')
arr = f.read().splitlines()
ans = 0
c = 0
for y, line in enumerate(arr):
    for x, e in enumerate(line):
        if e == 'X':
            a, c = dfs(arr, y, x, c)
            ans += a

print(ans)
