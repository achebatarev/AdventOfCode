from dataclasses import dataclass
from copy import deepcopy
from pprint import pprint
from enum import Enum
import sys

class Action(Enum):
    on = 'turn on'
    off = 'turn off'
    toggle = 'toggle'


@dataclass
class Point:
    y: int
    x: int

@dataclass
class Command:
    y: Point 
    x: Point 
    action: Action 
    
class Second:
    def __init__(self):
        self.board = [[0]*1000 for _ in range(1000)]
   
    def count(self):
        counter = 0
        for line in self.board:
            for cell in line:
                counter += cell 

        return counter

    def solve(self):
        data = parse()
        for command in data:
            range_y = command.y.y - command.x.y
            range_x = command.y.x - command.x.x 
            for y in range(range_y+1):
                for x in range(range_x+1):
                    pos_y = command.x.y + y
                    pos_x = command.x.x + x
                    if command.action == Action.on:
                        self.board[pos_y][pos_x] += 1
                    elif command.action == Action.off:
                        self.board[pos_y][pos_x] -= 1 if self.board[pos_y][pos_x] > 0 else 0 
                    else:
                        self.board[pos_y][pos_x] += 2
        return self.count()

class First:
    def __init__(self):
        self.board = [[0]*1000 for _ in range(1000)]
   
    def count(self):
        counter = 0
        for line in self.board:
            for cell in line:
                if cell == 1:
                    counter += 1

        return counter

    def solve(self):
        data = parse()
        for command in data:
            range_y = command.y.y - command.x.y
            range_x = command.y.x - command.x.x 
            for y in range(range_y+1):
                for x in range(range_x+1):
                    pos_y = command.x.y + y
                    pos_x = command.x.x + x
                    if command.action == Action.on:
                        self.board[pos_y][pos_x] = 1
                    elif command.action == Action.off:
                        self.board[pos_y][pos_x] = 0
                    else:
                        if self.board[pos_y][pos_x] == 0:
                            self.board[pos_y][pos_x] = 1
                        else:
                            self.board[pos_y][pos_x] = 0
        return self.count()


def parse():
    data = []
    with open(sys.argv[1]) as f:
        for line in f.readlines():
            inp = line.strip().split(',')
            inp = [x.split() for x in inp]
            point_x = Point(int(inp[0][-1]), int(inp[1][0]))
            point_y = Point(int(inp[1][-1]), int(inp[2][0]))
            action = ''
            if len(inp[0]) == 3 and inp[0][1] == 'on':
                action = Action.on
            elif len(inp[0]) == 3 and inp[0][1] == 'off':
                action = Action.off
            else:
                action = Action.toggle
            data.append(Command(point_y, point_x, action))
    return data

if __name__ == '__main__':
    first = First()
    second = Second()

    print(len(first.board), len(first.board[0]))
    print(first.solve())
    print(second.solve())
