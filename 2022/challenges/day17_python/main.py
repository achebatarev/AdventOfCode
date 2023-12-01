import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
from dataclasses import dataclass

# so I ll be given directions
# and then I ll be throwing shapes into a 7 units wide space, and left edge is 2 untis away from left wall, that are 3 untis above the highest rock
# Then I just execute horizontal direction followed by a vertical drop, if vertical drop is not feasible, I stop
# I do this for 2022 shapes 
# How would I be tracking where the rock is currently located, since they all have different shapes
# I can create 4 shapes classes, with the same method, for checking vertical move, or checking horizontal move
# I need to know where each shape is currently located, and being able to initilize them by simply giving a bottom position
try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'

def read_data(filename: str):
    with open(filename, 'r') as f:
        return f.read().strip()

@dataclass
class Shape:
    y: int
    size: int
    x: int = 2

    def move_vertically(self):
        self.y += 1
        
    def move_horizontally(self, direction):
        if direction == '<':
            self.x -= 1
        else:
            self.x += 1

    def top(self):
        return self.y - self.size + 1


@dataclass
class Minus(Shape):
    size: int = 1
    #Good
    def check_horizontally(self, matrix, direction) -> bool:
        for i in range(4):
            if direction == '<':
                if self.x+i-1 < 0 or matrix[self.y][self.x+i-1] != '.':
                    return False
            else:
                if self.x+i+1 >= 7 or matrix[self.y][self.x+i+1] != '.':
                    return False
        return True 

    #Good
    def check_vertically(self, matrix) -> bool:
        for i in range(4):
            if matrix[self.y+1][self.x+i] != '.':
                return False
        return True

    #Good
    def draw(self, matrix):
        for i in range(4):
            matrix[self.y][self.x+i] = '#'

@dataclass
class Plus(Shape):
    size: int = 3

    # Good
    def check_horizontally(self, matrix, direction) -> bool:
        for i in range(3):
            if direction == '<':
                if self.x-1 < 0: 
                    return False
                if matrix[self.y-i][self.x] != '.': 
                    return False
                if matrix[self.y-1][self.x-1+i] != '.':
                    return False
            else:
                if self.x+3 >= len(matrix[0]):
                    return False
                if matrix[self.y-i][self.x+2] != '.':
                    return False
                if matrix[self.y-1][self.x+1+i] != '.':
                    return False
        return True 

    # good
    def check_vertically(self, matrix) -> bool:
        if matrix[self.y+1][self.x+1] != '.':
            return False
        if matrix[self.y][self.x] != '.' or matrix[self.y][self.x+2] != '.':
            return False
        return True

    # Good
    def draw(self, matrix):
        for i in range(3):
            matrix[self.y-1][self.x+i] = '#'
            matrix[self.y-i][self.x+1] = '#'

@dataclass
class Boot(Shape):
    size: int = 3

    # Good
    def check_horizontally(self, matrix, direction) -> bool:
        for i in range(3):
            if direction == '<':
                if self.x-1 < 0 or matrix[self.y-i][self.x+1] != '.' or matrix[self.y][self.x+i-1] != '.':
                    return False
            else:
                if self.x+3 >= len(matrix[0]) or matrix[self.y-i][self.x+3] != '.' or matrix[self.y][self.x+i+1] != '.':
                    return False
        return True 

    # Good
    def check_vertically(self, matrix) -> bool:
        for i in range(3):
            if matrix[self.y+1][self.x+i] != '.':
                return False
        return True

    # Good
    def draw(self, matrix):
        for i in range(3):
            matrix[self.y][self.x+i] = '#'
            matrix[self.y-i][self.x+2] = '#'

@dataclass
class Stick(Shape):
    size: int = 4
    # Good
    def check_horizontally(self, matrix, direction) -> bool:
        for i in range(4):
            if direction == '<':
                if self.x-1 < 0 or matrix[self.y-i][self.x-1] != '.':
                    return False
            else:
                if self.x+1 >= len(matrix[0]) or matrix[self.y-i][self.x+1] != '.':
                    return False
        return True 

    # Good
    def check_vertically(self, matrix) -> bool:
        if matrix[self.y+1][self.x] != '.':
            return False
        return True
    # Good
    def draw(self, matrix):
        for i in range(4):
            matrix[self.y-i][self.x] = '#'

@dataclass
class Block(Shape):
    size: int = 2

    # Good
    def check_horizontally(self, matrix, direction) -> bool:
        for i in range(2):
            if direction == '<':
                if self.x-1 < 0 or matrix[self.y-i][self.x-1] != '.' or matrix[self.y-i][self.x] != '.':
                    return False
            else:
                if self.x+2 >= len(matrix[0]) or matrix[self.y-i][self.x+1] != '.' or matrix[self.y-i][self.x+2] != '.':
                    return False
        return True 

    # Good
    def check_vertically(self, matrix) -> bool:
        for i in range(2):
            if matrix[self.y+1][self.x+i] != '.':
                return False
        return True
    # Good
    def draw(self, matrix):
        for i in range(2):
            matrix[self.y-i][self.x] = '#'
            matrix[self.y-i][self.x+1] = '#'

# How am I calculating hwo high my tower is
# my highest is the number of free distance between empty space and taken space 
# test seem to work for first few rocks, but then it fails in grand scheme of things
# Problems:
#   Wrong way of calculating the height given, the closest to 0 point, and the size of the matrix in y direction | GOOD
#   Directions wrapping is wrongs 
#   some of the implemintation above is off
def partA(data):
    n, m = 7, 10000 
    highest = m - 1
    matrix = [['.']* n for _ in range(m)]
    matrix[-1] = ['#'] * n
    moves = 0
    k = 2022 
    shapes = [Minus, Plus, Boot, Stick, Block]
    for i in range(k):
        shape = shapes[i%len(shapes)](y=highest-4)
        while True:
            direction = data[moves % len(data)]  
            moves += 1
            if shape.check_horizontally(matrix, direction):
                shape.move_horizontally(direction)

            if not shape.check_vertically(matrix):
                break

            shape.move_vertically()

        shape.draw(matrix)
        highest = min(shape.top(), highest)

        #for line in matrix:
            #print(*line, sep='  ')
        #print(moves, highest, m - highest - 1)

    return m - highest - 1
# Ideas:
# There could be a repetition that we can abuse to skip a lot of computation
#   To identify, we need to keep track of motion we are on, the landscape, and the shape
# Maybe there is a way to identify where the block will land, based on the motions, so do not have to do it step by step
#   But we will still have to go though k cycles, which is just too much
# I can reuse the same space, since there is no need to know about it
#   But identifying it, and then, actually, reconfiguring the space, might not be worth it
#
# What are other ideas to not do k cycles
#   Width is only 7 and that can be abusable
# Also, can try getting rid of a matrix completely, the only thing I need to track of is the landscape
# If I track landscape, I migth even hit a repetition, but no certainty there
def partB(data):
    n, m = 7, 1000000000000000
    highest = m - 1
    matrix = [['.']* n for _ in range(m)]
    matrix[-1] = ['#'] * n
    moves = 0
    k = 1000000000000
    shapes = [Minus, Plus, Boot, Stick, Block]
    for i in range(k):
        shape = shapes[i%len(shapes)](y=highest-4)
        while True:
            direction = data[moves % len(data)]  
            moves += 1
            if shape.check_horizontally(matrix, direction):
                shape.move_horizontally(direction)

            if not shape.check_vertically(matrix):
                break

            shape.move_vertically()

        shape.draw(matrix)
        highest = min(shape.top(), highest)

        #for line in matrix:
            #print(*line, sep='  ')
        #print(moves, highest, m - highest - 1)

    return m - highest - 1

def parse_data(data):
    return data

data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
