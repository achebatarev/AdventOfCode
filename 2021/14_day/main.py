from collections import defaultdict, Counter
def first(template, repl):
    for w in range(10):
        new_template = []
        for i in range(1, len(template)):
            new_template.append(template[i-1])
            new_template.append(repl[template[i-1] + template[i]])
        new_template.append(template[i])
        template = ''.join(new_template)
        #if w < 7:
            #print(template)
    c = Counter(template)
    return max(c.values()) - min(c.values())

def second(template, repl):
    pairs = defaultdict(int)
    # store pair and next letter: probelm after a while the next letter will be lost or not
    for i in range(1, len(template)):
        pairs[template[i-1] + template[i]] += 1
    for _ in range(40):
        new_pairs = defaultdict(int)
        for i, pair in enumerate(pairs):
            #print(pairs[pair[0] + repl[pair]])
            n = pairs[pair]
            #print(pair, f_new, s_new)
            new_pairs[pair[0] + repl[pair]] += n
            new_pairs[repl[pair] + pair[1]] += n 

        pairs = new_pairs.copy()

    tr = defaultdict(int)
    for key, value in pairs.items():
        tr[key[1]] += value

    tr[template[0]] += 1   
    return max(tr.values()) - min(tr.values())

repl = {}
with open('input') as f:
    template = f.readline().strip()
    f.readline()
    while True:
        line = f.readline()
        if not line:
            break
        t, s = line.strip().split(' -> ')
        repl[t] = s
print(first(template, repl))
print(second(template, repl))


