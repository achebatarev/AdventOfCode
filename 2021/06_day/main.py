import sys
from collections import Counter, defaultdict

sys.setrecursionlimit(15000)
def first(inp):
    l = inp 
    for _ in range(80):
        inp = l[:]
        for i, n in enumerate(inp):
            if n == 0:
                l.append(8)
                l[i] = 6
            else:
                l[i] -= 1

    return len(l)
def second(inp):
    states = Counter(inp) 
    for _ in range(256):
        # when state is not 0, move all the numbers to state - 1 
        # if state == 0 
        new_states = defaultdict(int)
        for i in range(8, -1, -1):
            if i != 0:
                new_states[i-1] = states[i]
            else:
                new_states[6] += states[i]
                new_states[8] += states[i]
        states = new_states.copy()
        
    return sum(states.values())

    
    
    




with open('input', 'r') as f:
    inp = list(map(int, f.readline().split(',')))
#print(first(inp))
print(second(inp))

