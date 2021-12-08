from dataclasses import dataclass
from collections import defaultdict
def first(l_pairs) -> int:
    d = defaultdict(int) 
    # need to find a way to make pair1 == pair2 by storing the intermidiary values in d
    # need to consider only vertical and horizontal lines
    for pairs in l_pairs:
        pair1 = list(pairs.pair1)
        pair2 = list(pairs.pair2)
        if pair1[1] == pair2[1]:
            while pair1[0] != pair2[0]:
                d[tuple(pair1)] += 1
                if pair1[0] < pair2[0]:
                    pair1[0] += 1
                else:
                    pair1[0] -= 1
            d[tuple(pair1)] += 1

        elif pair1[0] == pair2[0]:
            while pair1[1] != pair2[1]:
                d[tuple(pair1)] += 1
                if pair1[1] < pair2[1]:
                    pair1[1] += 1
                else:
                    pair1[1] -= 1
            d[tuple(pair1)] += 1

    s = 0
    for key, item in d.items():
        if item >= 2: 
            s += 1
    return s

def second(l_pairs):
    d = defaultdict(int)
    for pairs in l_pairs:
        pair1 = list(pairs.pair1)
        pair2 = list(pairs.pair2)
        if pair1[1] == pair2[1]:
            while pair1[0] != pair2[0]:
                d[tuple(pair1)] += 1
                if pair1[0] < pair2[0]:
                    pair1[0] += 1
                else:
                    pair1[0] -= 1
            d[tuple(pair1)] += 1
        elif pair1[0] == pair2[0]:
            while pair1[1] != pair2[1]:
                d[tuple(pair1)] += 1
                if pair1[1] < pair2[1]:
                    pair1[1] += 1
                else:
                    pair1[1] -= 1
            d[tuple(pair1)] += 1
        else:
            while pair1[0] > pair2[0]:
                d[tuple(pair1)] += 1
                if pair1[1] < pair2[1]:
                    pair1[0] -= 1
                    pair1[1] += 1
                elif pair1[1] > pair2[1]:
                    pair1[0] -= 1
                    pair1[1] -= 1
            while pair1[0] < pair2[0]:
                d[tuple(pair1)] += 1
                if pair1[1] < pair2[1]:
                    pair1[0] += 1
                    pair1[1] +=1
                elif pair1[1] > pair2[1]:
                    pair1[0] += 1
                    pair1[1] -= 1
            d[tuple(pair1)] += 1
        
    s = 0
    for key, item in d.items():
        if item >= 2: 
            s += 1
    return s
                
                

@dataclass
class pairs:
    pair1: tuple 
    pair2: tuple 

d = {}
l = []
with open('input', 'r') as f:
    for line in f.readlines():
        data = line.strip().split(' -> ')
        pair1 = tuple(map(int, data[0].split(',')))
        pair2 = tuple(map(int, data[1].split(',')))
        d[pair1] = pair2 
        l.append(pairs(pair1, pair2))

print(first(l))
print(second(l))


