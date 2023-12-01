input = open('input.in', 'r').read().splitlines()
matrix = []
trees = set()

for x in input:
    matrix.append(list(map(int, list(x))))

visible = [[False] * len(matrix[0]) for _ in range(len(matrix))]

for y, line in enumerate(matrix):
    b = -1
    for x, tree in enumerate(line):
        if tree > b:
            visible[y][x] = True
            trees.add(f'y={y},x={x}')
            b = tree

for y, line in enumerate(matrix):
    b = -1
    for x, tree in reversed(list(enumerate(line))):
        if tree > b:
            visible[y][x] = True
            trees.add(f'y={y},x={x}')
            b = tree

for y, line in enumerate([*zip(*matrix)]):
    b = -1
    for x, tree in enumerate(line):
        if tree > b:
            visible[x][y] = True
            trees.add(f'y={x},x={y}')
            b = tree

for y, line in enumerate([*zip(*matrix)]):
    b = -1
    for x, tree in reversed(list(enumerate(line))):
        if tree > b:
            visible[x][y] = True
            trees.add(f'y={x},x={y}')
            b = tree


result = 0
for line in visible:
    for e in line:
        if e:
            result += 1
print(result)
print(len(trees))