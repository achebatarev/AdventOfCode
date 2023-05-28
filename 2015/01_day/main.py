def first(inp):
    r = 0
    for e in inp:
        if e == '(':
            r += 1
        elif e == ')':
            r -= 1
    return r

def second(inp):
    r = 0
    for i,e in enumerate(inp):
        if e == '(':
            r += 1
        elif e == ')':
            r -= 1
        if r < 0:
            return i+1

    return r

with open('input.txt') as f:
    data = f.read()
print(first(data.strip()))
print(second(data.strip()))
