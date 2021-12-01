from functools import lru_cache

@lru_cache()
def perm(high, adapters, last):
    a = 0
    if high == last:
        return 1
    else:
        for i in range(1, 4):
            if last + i in adapters:
               a += perm(high, adapters, last+i)
        return a

adapters = set() 
with open('input.txt') as f:
    for line in f.readlines():
        adapters.add(int(line.strip()))

last = 0
a = perm(max(adapters), tuple(adapters), last)
print(a)
