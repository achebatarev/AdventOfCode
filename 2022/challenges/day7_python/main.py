import sys
from pprint import pprint
from dataclasses import dataclass
from collections import defaultdict, deque, Counter
import heapq

try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'

FILETYPE, DIR = 'FILE', 'DIR'
ls, cd = 'ls', 'cd'

class Node:
    def __init__(self, name, type=DIR, parent=None, size=None):
        self.name = name
        self.type = type 
        self.size = size
        self.children = []
        self.parent = parent

    def __str__(self):
        return f'Name: {self.name}, Type: {self.type}, Parent: {self.parent.name if self.parent else None}, Children: {self.children}'
    __repr__ = __str__

def read_data(filename: str):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data



def move(current_folder, destination):
    global root
    if current_folder.name == destination and destination == '/':
        return current_folder
    elif destination == '..':
        return current_folder.parent
    elif destination == '/':
        return root
    else:
        for child in current_folder.children:
            if child.name == destination:
                return child 

        raise Exception(f'can not cd into folder {destination} from {current_folder.name}')
    

def list_files(current_folder, data):
    while data and (not data[0].startswith('$')):
        line = data.popleft()
        size = None
        name = None
        if line.startswith('dir'):
            name = line.split()[1]
            filetype = DIR 
        else:
            size, name = line.split()
            size = int(size)
            filetype = FILETYPE
        current_folder.children.append(Node(name, parent=current_folder, size=size, type=filetype))

def dfs(node):
    global result
    if node.type == FILETYPE:
        return node.size 
    total = 0
    for child in node.children:
        total += dfs(child)

    if total <= 100000:
        result += total 

    return total

def partA(data):
    global result, total_space
    result = 0 
    total_space = dfs(data)
    return result

#def check(part):
    #if part == 'A':
        #if total >= 1000000:
            #result += total 
    #elif part == 'B'
def dfs2(node):
    global ans, need
    if node.type == FILETYPE:
        return node.size 
    total = 0
    for child in node.children:
        total += dfs2(child)
    if total >= need:
        ans = min(ans, total)

    return total

def partB(data):
    global total_space, need, ans
    have = 70000000 - total_space
    need = 30000000 - have
    ans = float('inf') 
    dfs2(data)
    return ans

def parse_data(data):
    global root
    current_folder = Node('/') 
    root = current_folder
    data = deque(data)
    while data:
        command = data.popleft().split()
        if command[1] == ls:
            list_files(current_folder, data)
        elif command[1] == cd:
            current_folder = move(current_folder, command[2])
    return root 

data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
