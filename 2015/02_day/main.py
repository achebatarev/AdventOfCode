def first(data):
    total = 0
    for l, w, h in data:
        lw =  l * w
        wh =  w * h
        hl =  h * l
        small_side = min(lw, wh, hl)
        total += small_side + (2*lw) + (2*wh) + (2*hl)
    return total
def second(data):
    total = 0
    for l, w, h in data:
        bow = l * w * h
        one, two = sorted([l, w, h])[:2]
        present_wrap = one + one + two + two
        total += bow + present_wrap
    return total

data = []
with open('input.txt') as f:
    for line in f.readlines():
        data.append(list(map(int, line.strip().split('x'))))

print(first(data))
print(second(data))
    
