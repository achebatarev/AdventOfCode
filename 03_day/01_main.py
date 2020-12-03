space = []
with open('input.txt') as f:
    for line in f.readlines():
        temp = list(line.strip())
        space.append(temp)
x = 0
y = 0
r = 0
while y < len(space):
    if space[y][x%len(space[0])] == '#':
        r += 1
    x+=3
    y+=1
print(r)
