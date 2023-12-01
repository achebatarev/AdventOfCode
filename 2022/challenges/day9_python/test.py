import sys
try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'

iN = open(FILE, 'r').read().splitlines()
h = [0, 0]
t = [[0,0] for _ in range(9)]
v = set()

def incrementer(h, d):
    if d == 'R':
        h[0] += 1
    elif d == 'L':
        h[0] -= 1
    elif d == 'U':
        h[1] += 1
    elif d == 'D':
        h[1] -= 1

def adjuster(b, f):
    xdiff = f[0] - b[0]
    ydiff = f[1] - b[1]
    # print(f'{xdiff if xdiff > 1 else ""}')
    if abs(xdiff) >= abs(ydiff):
        b[0] += max(xdiff, ydiff) 
    if abs(ydiff) >= abs(xdiff): 
        b[1] += max(xdiff, ydiff)
    return b
    
for l in iN:
    c = l.split()
    for i in range(int(c[1])):
        incrementer(h, c[0])
        for j in range(len(t)):
            if j == 0:
                adjuster(t[j], h)
            else:
                adjuster(t[j], t[j - 1])       
        v.add(str(t[-1][0]) + " " + str(t[-1][1]))
    
print(len(v))
#print(len(t))