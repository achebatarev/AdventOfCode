l = []
with open('input.txt') as f:
    for line in f.readlines():
        l.append(int(line.strip()))

for e1 in l:
    for e2 in l:
        for e3 in l:
            if (e1 + e2 + e3) == 2020:
                print(e1, e2, e3, e1*e2*e3)
