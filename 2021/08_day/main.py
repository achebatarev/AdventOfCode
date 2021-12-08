from collections import Counter
def first(out):
    s = set([2, 3, 4, 7])
    r = 0
    for line in out:
        for e in line:
            if len(e) in s:
                r += 1
    return r

def second(inp, out):
    d = {2: 1, 3: 7, 4: 4, 7: 8}
    r = 0
    for i, line in enumerate(inp):
        len_f = []
        len_s = []
        decode = [None] * 10
        for e in line:
            if len(e) in d:
                decode[d[len(e)]] = e
            elif len(e) == 5:
                len_f.append(e)
            else:
                len_s.append(e)
        decode[3] = find_n(decode[7], len_f)
        decode[9] = find_n(set(decode[7] + decode[4]), len_s)
        left_top = find_left_top(decode[3], decode[9], len_f) 
        decode[5] = [e for e in len_f if left_top in e][0] 
        decode[2] = [e for e in len_f if e != decode[5] and e != decode[3]][0]
        decode[6] = find_one(decode[1], len_s) 
        decode[0] = [e for e in len_s if e != decode[6] and e != decode[9]][0]
        n = []
        b = [Counter(e) for e in decode]
        for e in out[i]:
            c = Counter(e)
            for a,k in enumerate(b):
                if c == k:
                    n.append(a)
                    break
        r += int(''.join(list(map(str, n))))
    return r

def find_n(n, len_s):
    for e in len_s:
        s = set(e)
        for l in n:
            if l not in s:
                break
        else:
            return e

def find_one(n, len_s):
    for e in len_s:
        s = set(e)
        for l in n:
            if l not in s:
                return e

def find_left_top(three, nine, len_f):
    left_top = 0
    for e in three+nine:
        left_top ^= ord(e)
    return chr(left_top)


inp = []
out = []
with open('input', 'r') as f:
    for line in f.readlines():
        i, o = line.strip().split('|')
        inp.append(i.split())
        out.append(o.split())
print(first(out))
print(second(inp, out))

    
