from collections import deque
codes = []
goal = 0
preamble = deque()
with open('input.txt') as f:
    for i, line in enumerate(f.readlines()):
        num = int(line.strip())
        if i < 25:
            preamble.append(num)
        else:
            for e in preamble:
                if num - e in preamble:
                    break
            else:
                goal = num
            preamble.popleft()
            preamble.append(num)
        codes.append(num)

total = codes[0] + codes[1]
first = 0
i = 2
while i < len(codes):
    if total > goal:
        total -= codes[first]
        first += 1
    elif total < goal:
        total += codes[i]
        i += 1
    if total == goal:
        break

high = 0
low = max(codes) + 1
for j in range(first, i+1):
    high = max(high, codes[j])
    low = min(low, codes[j])
print(low + high)

