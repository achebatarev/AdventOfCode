from collections import defaultdict, deque
def first(inp):
    r = []
    wrong_lines = []
    mapping = {')': 3, ']': 57, '}': 1197, '>': 25137}
    mapping2 = {'[': ']', '(': ')', '{': '}', '<': '>'}
    for i, line in enumerate(inp):
        stack = deque()
        for e in line:
            if e in ('[({<'):
                stack.append(mapping2[e])
            else:
                bracket = stack.pop()
                if bracket != e:
                    r.append(e)
                    wrong_lines.append(i)
                    break
    return sum([mapping[e] for e in r]),wrong_lines

def second(inp, wrong_lines):
    mapping = {')': 1, ']': 2, '}': 3, '>': 4}
    mapping2 = {'[': ']', '(': ')', '{': '}', '<': '>'}
    response = []
    for i, line in enumerate(inp):
        if i not in wrong_lines:
            stack = deque()
            for e in line:
                if e in ('[({<'):
                    stack.append(mapping2[e])
                else:
                    stack.pop()
            score = 0
            while stack:
                bracket = stack.pop()
                score = (score * 5) + mapping[bracket]
            response.append(score)
    return sorted(response)[len(response)//2]


with open('input', 'r') as f:
    l = []
    for line in f.readlines():
        l.append(line.strip())

output, wrong_lines = first(l)
print(output)
print(second(l, set(wrong_lines)))
