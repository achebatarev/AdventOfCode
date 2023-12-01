import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
from dataclasses import dataclass
from copy import deepcopy
import functools
import operator
from typing import Any

try:
    FILE = sys.argv[1]
except:
    FILE = 'test.in'


@dataclass
class Operation:
    sign: str
    val: str


@dataclass
class Monkey:
    items: deque
    operation: Operation
    test: int
    passed: int
    not_passed: int
    inspected: int = 0


def read_data(filename: str):
    with open(filename, 'r') as f:
        return f.read().split('\n\n')


def partA(data):
    data = deepcopy(data)
    k = len(data)
    for i in range(20 * k):
        monkey = data[i % k]
        while monkey.items:
            item = monkey.items.popleft()
            if monkey.operation.sign == '+':
                if monkey.operation.val.isdigit():
                    item += int(monkey.operation.val)
                else:
                    item += item
            else:
                if monkey.operation.val.isdigit():
                    item *= int(monkey.operation.val)
                else:
                    item *= item
            item //= 3
            if item % monkey.test == 0:
                data[monkey.passed].items.append(item)
            else:
                data[monkey.not_passed].items.append(item)
            monkey.inspected += 1
    inspected = []
    for monkey in data:
        inspected.append(monkey.inspected)
    two = sorted(inspected, reverse=True)[:2]
    return two[0] * two[1]


def partB(data):
    k = len(data)
    mod = functools.reduce(operator.mul, [monkey.test for monkey in data])
    for i in range(10000 * k):
        monkey = data[i % k]
        while monkey.items:
            item = monkey.items.popleft()
            if monkey.operation.sign == '+':
                if monkey.operation.val.isdigit():
                    item += int(monkey.operation.val)
                else:
                    item += item
            else:
                if monkey.operation.val.isdigit():
                    item *= int(monkey.operation.val)
                else:
                    item *= item
            item %= mod
            if item % monkey.test == 0:
                data[monkey.passed].items.append(item)
            else:
                data[monkey.not_passed].items.append(item)
            monkey.inspected += 1
    inspected = []
    #pprint(data)
    for monkey in data:
        inspected.append(monkey.inspected)
    two = sorted(inspected, reverse=True)[:2]

    return two[0] * two[1]


def parse_data(data):
    monkeys = []
    for monkey in data:
        monkey = monkey.splitlines()
        items = deque(map(int, monkey[1].split(': ')[1].split(', ')))
        test = int(monkey[3].split()[-1])
        operation = Operation(*monkey[2].split()[-2:])
        passed = int(monkey[4].split()[-1])
        no_pass = int(monkey[5].split()[-1])
        monkeys.append(Monkey(items, operation, test, passed, no_pass))
    return monkeys


data = read_data(FILE)
parsed_data = parse_data(data)
print(partA(parsed_data))
print(partB(parsed_data))
