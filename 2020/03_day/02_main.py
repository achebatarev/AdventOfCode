def calc(right, down, space):
    x = 0
    y = 0
    result = 0
    while y < len(space):
        if space[y][x%len(space[0])] == '#':
            result += 1
        x += right
        y += down
    return result

space = []
with open('input.txt') as f:
    for line in f.readlines():
        temp = list(line.strip())
        space.append(temp)
answer = 1
instructions = [(1, 1), (3, 1), (5, 1), (7,1), (1,2)]
for right, down in instructions:
    answer *= calc(right, down, space)
print(answer)
