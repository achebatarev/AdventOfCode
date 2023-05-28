import sys
def is_nice1(w):
    vowels = {'a', 'e', 'i', 'o', 'u'} 
    there = 0 
    twice = False
    if w[0] in vowels:
        there += 1
    for i in range(1, len(w)):
        string = w[i-1] + w[i]
        if string in {'ab', 'cd', 'pq', 'xy'}:
            return False
        if w[i-1] == w[i]:
            twice = True
        if w[i] in vowels:
            there += 1

    if there >= 3 and twice:
        return True
    return False

def is_nice2(w):
    pair = False
    repeat = False
    d = {} 
    subs = []
    for i in range(1, len(w)):
        subs = w[i-1: i+1]
        if subs in d: 
            if subs != prev or d[subs] == i % 2:
                pair = True
        else:
            d[subs] = i % 2
        prev = subs

        if i+1 < len(w) and w[i-1] == w[i+1]:
            repeat = True
    return pair and repeat
    


        

def second(data):
    r = 0
    for string in data:
        if is_nice2(string):
            #print(string)
            r += 1
    return r


def first(data):
    r = 0
    for string in data:
        if is_nice1(string):
            r += 1

    return r

data = []

with open(sys.argv[1]) as f:
    for line in f.readlines():
        data.append(line.strip())
print(first(data))
#print(is_nice2('xxyxx'))
print(second(data))
            
