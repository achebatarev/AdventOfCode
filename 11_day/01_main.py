from copy import deepcopy
check = [(-1, 1), (-1,-1), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (1, 0)]
def check_seat(layout, x, y):
    count  = 0
    for r, c in check:
        xr, xc = y+r, x+c
        if 0 <= xr < len(layout) and 0 <= xc < len(layout[0]) and layout[xr][xc] == '#':
            count += 1
    return count

prev = []
layout = []
with open('input.txt') as f:
    for line in f.readlines():
        layout.append(list(line.strip()))

while(True):
    prev = deepcopy(layout) 
    for row, e in enumerate(prev):
        for column, cell in enumerate(e):
            if cell == 'L':
                if check_seat(prev, column, row) == 0:
                    layout[row][column] = '#'
            elif cell == '#':
                if check_seat(prev, column, row) >= 4:
                        layout[row][column] = 'L'
    if layout == prev:
        break

total = 0 
for row in layout:
    total += row.count('#')
print(total)

