adapters = []
with open('input.txt') as f:
    for line in f.readlines():
        adapters.append(int(line.strip()))

prev = 0
one = 0
three = 1
for adapter in sorted(adapters):
    jolt = adapter - prev
    if jolt == 1:
        one += 1
    elif jolt == 3:
        three += 1
    else:
        print(jolt)
    prev = adapter
print(one, three, one * three)
    

