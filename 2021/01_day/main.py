
def first(l):
    c = 0
    prev = l[0]
    for i in range(1, len(l)):
        if l[i] > prev:
            c += 1
        prev = l[i]
    return c

def second(l):
    l2 = []
    for i, e in enumerate(l):
        try:
            l2.append(sum(l[i:i+3]))
        except:
            break
    return first(l2)


    

if __name__ == '__main__':
    l = []
    with open('input', 'r') as f:
        for e in f.readlines():
            l.append(int(e.strip()))
    print(first(l))
    print(second(l))
