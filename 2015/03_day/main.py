def first(directions):
    s = set()
    start = (0,0)
    s.add(start)
    d = {'^': (1, 0), 'v': (-1, 0), '>': (0, 1), '<': (0, -1)}
    for direction in directions:
        y, x = d[direction]
        start = (y + start[0], x + start[1])
        s.add(start)
    return len(s)

def second(directions):
    s1 = set()
    s2 = set()
    start1 = (0,0)
    start2 = (0,0)
    s1.add(start1)
    s2.add(start2)
    d = {'^': (1, 0), 'v': (-1, 0), '>': (0, 1), '<': (0, -1)}
    for i, direction in enumerate(directions):
        y, x = d[direction]
        if i % 2 == 0:
            start1 = (y + start1[0], x + start1[1])
            s1.add(start1)
        else:
            start2 = (y + start2[0], x + start2[1])
            s2.add(start2)
    return len(s1.union(s2))

with open('input.txt') as f:
    instructions = f.read()

print(first(instructions.strip()))
print(second(instructions.strip()))
