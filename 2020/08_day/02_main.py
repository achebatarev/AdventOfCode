from copy import deepcopy
def run_program(instructions):
    i = 0
    acc = 0
    s = set()
    while i < len(instructions):
        if i in s:
            return (False, acc)    
        else:
            s.add(i)
        if instructions[i][0] == 'acc':
            acc += instructions[i][1]
        if instructions[i][0] == 'jmp':
            i += instructions[i][1]
        else:
            i += 1

    return (True, acc)

instructions = []
with open('input.txt') as f:
    for line in f.readlines():
        mnemonic, a = line.strip().split()
        instructions.append([mnemonic, int(a)])

for i, instruction in enumerate(instructions):
    if instruction[0] == 'jmp':
        copy_instr = deepcopy(instructions)
        copy_instr[i][0] = 'nop'
        result, acc = run_program(copy_instr)
        if result:
            print(acc)
            break
    elif instruction[0] == 'nop':
        copy_instr = deepcopy(instructions)
        copy_instr[i][0] = 'jmp'
        result, acc = run_program(copy_instr)
        if result:
            print(acc)
            break
        
