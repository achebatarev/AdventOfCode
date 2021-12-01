a = 0
s = set()
with open('input.txt') as f:
    for line in f.readlines():
        if line != '\n':
            for l in line.strip():
                if l not in s:
                    a += 1
                    s.add(l)
        else:
            s = set()
print(a)

          
