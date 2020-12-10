from collections import deque
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
                print(num)
            preamble.popleft()
            preamble.append(num)

