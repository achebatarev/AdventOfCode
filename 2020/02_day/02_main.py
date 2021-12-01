a = 0 
with open('input.txt') as f:
    for line in f.readlines():
        pos, l, w = line.split(" ")
        l = l[0]
        pos1, pos2 = map(int, pos.split('-'))
        if w[pos1-1] == l or w[pos2-1] == l:
            if not (w[pos1-1] == l and w[pos2-1] == l):
                a += 1
    print(a)
