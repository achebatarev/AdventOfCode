mapping = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1))
def dfs(arr, y, x, count):
    res = 0
    for r, c in mapping:
        yr = y
        xc = x
        l = []
        for _ in range(4):
            if 0 <= yr < len(arr) and 0 <= xc < len(arr[0]):
                l.append(arr[yr][xc])
            yr = yr+r
            xc = xc+c
        if ''.join(l) == 'XMAS':
            res += 1
            count+=1
    return res, count

def dfs2(arr, y, x):
    # I need to check these relative locations and make sure that it has 'M', 'S' present
    left = ((1, 1), (-1, -1))
    right = ((1, -1), (-1, 1))
    ll = []
    lr = []
    for r, c in left:
        if 0 <= y+r < len(arr) and 0 <= x+c < len(arr[0]):
            ll.append(arr[y+r][x+c])
    for r, c in right:
        if 0 <= y+r < len(arr) and 0 <= x+c < len(arr[0]):
            lr.append(arr[y+r][x+c])
    print(sorted(ll), sorted(lr), int(True))
    return int(sorted(ll)== sorted(lr) and sorted(ll) == ['M', 'S']) 

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


f = open('input.d4')
arr = f.read().splitlines()
ans = 0
c = 0
for y, line in enumerate(arr):
    for x, e in enumerate(line):
        if e == 'A':
            ans += dfs2(arr, y, x)
print(ans)


