from collections import deque, defaultdict
def first(matrix):
    return recursive_first(matrix, 'start') 

def recursive_first(matrix, node, visited=None, path=None):
    if not path:
        path = []
    if not visited:
        visited = []
    if node == 'end':
        path.append('end')
        return 1
    kids = matrix[node]
    score = 0
    for child in kids:
        if child not in visited:
            if node.islower() and node != 'end':
                score += recursive_first(matrix, child, visited + [node], path + [node])
            else:
                score += recursive_first(matrix, child, visited, path + [node])

    return score

def second(matrix):
    return recursive_second(matrix, 'start')

def recursive_second(matrix, node, visited=None, path=None ):
    if not path:
        path = []
    if not visited:
        visited = defaultdict(int)
    if node == 'end':
        path.append('end')
        print(path)
        return 1
    if node.islower() and visited[node] >= 1 and any(val >= 2 for val in visited.values()):
        return 0
    kids = matrix[node]
    score = 0
    for child in kids:
        # check if a small cave and if any cave was visited twice before
        if child != 'start':
            v = visited.copy()
            if node.islower():
                v[node] += 1
            score += recursive_second(matrix, child, v, path + [node])
    return score
            
            


    
    


d = defaultdict(list) 
with open('input') as f:
    for line in f.readlines():
        key, value = line.strip().split('-')
        d[key].append(value)
        d[value].append(key)

print(first(d))
print(second(d))
