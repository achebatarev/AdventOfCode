instructions = []
with open('input.txt') as f:
    for line in f.readlines():
        mnemonic, a = line.strip().split(' ')
        instructions.append((mnemonic, int(a)))

acc = 0
i = 0
s = set()
while i < len(instructions):
    if i in s:
        break
    else:
        s.add(i)
    
    if instructions[i][0] == 'acc':
        acc += instructions[i][1]

    if instructions[i][0] == 'jmp':
        i += instructions[i][1]
    else:
        i += 1

print(acc)
