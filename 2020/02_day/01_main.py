from collections import Counter
a = 0
with open('input.txt') as f:
    for line in f.readlines():
        ran, l, p = line.split(" ")
        l = l[0]
        low, high = map(int, ran.split("-"))
        c = Counter(p)
        if c[l] >= low and c[l] <= high:
            a += 1
    print(a)

        

