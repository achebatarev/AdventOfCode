import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
from dataclasses import dataclass
import heapq

try:
    FILE = sys.argv[1]
except:
    FILE = "test.in"


def read_data(filename: str):
    with open(filename, "r") as f:
        return f.read().splitlines()


def first(data):
    a = 0
    for l in data:
        b = ""
        for i in l:
            if i.isdigit():
                b += i
                break

        for i in l[::-1]:
            if i.isdigit():
                b += i
                break
        a += int(b)

    return a


def second(data):
    a = 0
    d = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }

    for s in data:
        l = []
        for e in d:
            y = s.find(e)
            while y != -1:
                l.append((e, y))
                y = s.find(e, y + 1)
        c = int(d[min(l, key=lambda x: x[1])[0]] + d[max(l, key=lambda x: x[1])[0]])
        a += c

    return a


def parse_data(data):
    return data


data = read_data(FILE)
parsed_data = parse_data(data)
# print(first(parsed_data))
print(second(parsed_data))
