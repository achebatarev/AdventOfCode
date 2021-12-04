from collections import defaultdict
def first(inp):
    l = [defaultdict(int) for _ in range(len(inp[0]))]
    for e in inp: 
        for i in range(len(e)):
            l[i][e[i]] += 1
    r = []
    for d in l:
        r.append(max(d.items(), key=lambda x: x[1])[0])
    b = ''.join(r)
    gamma = int(b, 2)
    epsilon = int(''.join('1' if x == '0' else '0' for x in b), 2)
    return gamma * epsilon

def second(inp):
    ogr = csr = inp
    length = inp[0]
    pos = 0
    while pos < len(length):
        print(ogr, csr, pos, len(length))
        if len(ogr) > 1:
            highest_bit, lowest_bit = get_highest_lowest_bit(ogr, pos, True)
            ogr = get_bit_list(ogr, highest_bit, pos)
        
        if len(csr) > 1:
            highest_bit, lowest_bit = get_highest_lowest_bit(csr, pos, False)
            csr = get_bit_list(csr, lowest_bit, pos)
        pos += 1
    return int(''.join(ogr), 2) * int(''.join(csr), 2)

        

    
def get_highest_lowest_bit(inp, pos, who):
    d = defaultdict(int)
    for e in inp:
        d[e[pos]] += 1
    # d has highest and the lowest bit
    if d['1'] == d['0'] and who:
        h = '1'
        l = '0'
    elif d['1'] == d['0'] and not who:
        h = '1'
        l = '0'
    elif d['1'] < d['0']:
        h = '0'
        l = '1'
    else:
        h = '1'
        l = '0'

    return h, l

def get_bit_list(inp, bit, pos):
    r = []
    for e in inp:
        if e[pos] == bit:
            r.append(e)
    return r
            



with open('input', 'r') as f:
    inp = []
    for line in f.readlines():
        inp.append(line.strip())
print(first(inp))
print(second(inp))
