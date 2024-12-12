from collections import defaultdict
rules = defaultdict(list) 

def is_secure(arr: list[int]) -> bool:
    secure = 0
    for i, e in enumerate(arr):
        for j in range(i+1, len(arr)):
            if arr[j] in rules[e]:
                break
        else:
            secure += 1

    return secure == len(arr)

def move_element(arr, old_pos, new_pos):
    l = []
    for i, e in enumerate(arr):
        if i == new_pos:
            l.append(arr[old_pos])
        elif i == old_pos:
            continue
        l.append(e)
    return l



f = open('input.d5')
r, inp = f.read().split('\n\n')
for line in r.splitlines():
    x, y = line.split('|')
    rules[int(y)].append(int(x))

def part1(inp):
    ans = 0
    for line in inp.splitlines():
        arr = list(map(int, line.split(',')))
        if is_secure(arr):
            ans += arr[len(arr)//2]
    return ans

def part2(inp):
    ans = 0
    for line in inp.splitlines():
        arr = list(map(int, line.split(',')))
        changed = False
        while not is_secure(arr):
            # TODO: I gotta make this secure... how?
            # Find non secure element, and change it's position
            # can I make a sorter?
            # the dumb way, take a wrong element, and put it in front of current element that' being checked
            changed = True
            breaking = False
            for i, e in enumerate(arr):
                for j in range(i+1, len(arr)):
                    if arr[j] in rules[e]:
                        arr = move_element(arr, j, i)
                        breaking = True 
                        break
                if breaking:
                    break
        if changed:
            ans += arr[len(arr)//2]


    return ans


print(part1(inp))
print(part2(inp))


            
