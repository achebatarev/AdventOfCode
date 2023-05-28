import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
import math
from dataclasses import dataclass, field
import operator
from typing import Any, List, Optional

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'


@dataclass
class Node:
    type: str
    contents: Optional[str] = None
    children: List[Any] = field(default_factory=lambda: [])


def read_data(filename: str):
    with open(filename, 'r') as f:
        return f.read().strip()


#Stream
# Group, Garbage
# Garbage no nesting, ! ignored next
# Okey, so I can collect garbage, and I can collect groups
# groups can be represented as a tree, or just traverse it
# I think I will just construct tree and then traverse it getting myself the answer
def partA(root):
    q = deque([root])
    res = 0
    layer = 1
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            #print(layer, node)
            if node.type == 'group':
                res += layer
            for child in node.children:
                q.append(child)
        layer += 1
    return res


def partB(root):
    q = deque([root])
    res = 0
    layer = 1
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            print(layer, node)
            if node.type == 'garbage':
                res += len(node.contents)
            for child in node.children:
                q.append(child)
        layer += 1
    return res
    pass


def parser(data) -> List[Node]:
    children = []
    while data:
        char = data.popleft()
        #print(char, children)
        if char == ',':
            continue

        elif char == '{':
            node = Node('group')
            node.children = parser(data)
            children.append(node)

        elif char == '}':
            return children

        #parse garbage code
        elif char == '<':
            content = []
            while data and char != '>':
                char = data.popleft()

                if char == '!':
                    data.popleft()
                    continue
                if char == '>':
                    continue
                content.append(char)
            node = Node('garbage', ''.join(content))
            children.append(node)

    return children


# I wanna do it recursively, where { will create a node
def parse_data(data):
    data = deque(data)
    return parser(data)[0]


if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(partA(parsed_data))
    print(partB(parsed_data))
