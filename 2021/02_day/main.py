def first(inp):
    y = 0
    x = 0
    add = lambda z, v: z + v
    subtract = lambda z, v: z - v
    d = {'down': add, 'up': subtract}
    for e in inp:
        direction, value = e.split()
        if direction in d:
            y = d[direction](y, int(value))
        else: 
            x += int(value)
    return x*y

def second(inp):
    y = x = aim = 0
    add = lambda z, v: z + v
    subtract = lambda z, v: z - v
    d = {'down': add, 'up': subtract}
    for e in inp:
        direction, value = e.split()
        value = int(value)
        if direction in d:
            aim = d[direction](aim, value)
        else:
            x += value
            y += (value * aim)
    return y * x
        

inp = []
with open('input', 'r') as f:
    for e in f.readlines():
        inp.append(e.strip())

#inp = ['forward 5','down 5','forward 8','up 3','down 8','forward 2']
print(first(inp))
print(second(inp))
        
