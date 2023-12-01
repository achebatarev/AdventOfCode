from typing import List
import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
from dataclasses import dataclass
import curses

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'


def draw(screen, y=0, x=0, text=" ", color=1) -> None:
    stdscr.addstr(y, x, text, curses.color_pair(color))
    screen.refresh()


@dataclass
class Point:
    y: int
    x: int

    def __sub__(self, other):
        return Point(self.y - other.y, self.x - other.x)


@dataclass
class Move:
    direction: str
    amount: int


# every instruction, I move H to the new location
# Then I need to move T to H
# I check if H and T are adjacent
# adjacency just means that difference between coords is not more than 1 in both x and y planes
# If not adjacent I need to move T to H
# if both x and y are different then I can move diagonally to get faster to H
# else I just move 1 by 1 and add everything to set
def partA(data: List[Move]) -> int:
    s = set()
    H = Point(0, 0)
    T = Point(0, 0)
    s.add(str(T))
    for move in data:
        if move.direction == 'R':
            H.x += move.amount
        elif move.direction == 'L':
            H.x -= move.amount
        elif move.direction == 'U':
            H.y -= move.amount
        elif move.direction == 'D':
            H.y += move.amount
        move_knot(H, T, s)
    return len(s)


def move_knot(H: Point, T: Point, s=None) -> None:
    global arr
    diff = H - T
    # while loop only needed for partA
    while abs(diff.x) > 1 or abs(diff.y) > 1:
        if diff.y != 0:
            if diff.y < 0:
                T.y -= 1
            else:
                T.y += 1
        if diff.x != 0:
            if diff.x < 0:
                T.x -= 1
            else:
                T.x += 1
        if s:
            s.add(str(T))
        diff = H - T


# Put all of the knots connected to head into arr, and then just do the operation above
# for each individual knot
# we only had H and T, and we just have a lot more H and T, but only the last one is a tail
def partB(data) -> int:
    global arr
    s = set()
    knots = [Point(4, 0) for _ in range(10)]
    s.add(str(knots[-1]))
    for move in data:
        for _ in range(move.amount):
            H = knots[0]

            if move.direction == 'R':
                H.x += 1
            elif move.direction == 'L':
                H.x -= 1
            elif move.direction == 'U':
                H.y -= 1
            elif move.direction == 'D':
                H.y += 1
            #draw(screen, H.y, H.x, 'H')

            for i, knot in enumerate(knots[1:]):
                if knots[-1] is knot:
                    move_knot(H, knot, s)
                else:
                    move_knot(H, knot)
                H = knot
    return len(s)


def parse_data(data) -> List[Move]:
    ans = []
    for e in data:
        d, q = e.split()
        ans.append(Move(d, int(q)))
    return ans


def read_data(filename: str) -> List[str]:
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data


def set_curses_setting() -> None:
    stdscr.clear()
    #curses.beep()
    curses.curs_set(0)
    if curses.has_colors():
        curses.start_color()
    # text, background
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)


def main(screen) -> None:
    set_curses_setting()
    height, width = screen.getmaxyx()
    data = read_data(FILE)
    parsed_data = parse_data(data)
    while True:
        partB(parsed_data, screen)
    #stdscr.refresh()


if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(partA(parsed_data))
    print(partB(parsed_data))
    #stdscr = curses.initscr()
    #curses.wrapper(main)