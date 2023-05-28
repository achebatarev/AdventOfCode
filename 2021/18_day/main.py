import ast
from copy import deepcopy
from os import replace
import math
from pprint import pprint


def first(l):
    first_line = l[0]
    for i in range(1, len(l)):
        first_line = addition(first_line, l[i])
        first_line = reduce_number(first_line)

    return count_magnitude(first_line)

def second(l):
    magnitude = 0
    for i, first in enumerate(l):
        for j, second in enumerate(l):
            if i != j:
                result = addition(first, second)
                reduced = reduce_number(result)
                magnitude = max(magnitude, count_magnitude(reduced))
    return magnitude 

def reduce_number(l):
    number = deepcopy(l)
    prev = None
    while number != prev:
        prev = deepcopy(number)
        prev_split = None
        while find_depth(number) >= 5:
            number = explode(number)
            #print('after explode', number)
        while prev_split != number:
            prev_split = deepcopy(number)
            number = split(number)[0]
            #print('after split', number)
            while find_depth(number) >= 5:
                number = explode(number)
                #print('after explode', number)
    return number 

def addition(l1, l2):
    new_l = []
    new_l.append(l1)
    new_l.append(l2)
    return new_l

def explode(l):
    li, n_to_add, _, target  = depth(l, 0, None, 0, None, 3)
    if target:
        return modify_item(li, 0, target, n_to_add)[0]
    return li

def find_depth(l):
    if isinstance(l, list):
        return 1 + max(find_depth(item) for item in l)
    else:
        return 0

def depth(l, k, n_to_add, index, target_index,b):
    new_l = []
    for item in l:
        if isinstance(item, list) and k == b and not target_index:
            pair, n_to_add, direction = explode_pair(l)
            target_index = index + direction 
            index += 1
            return pair, n_to_add, index, target_index
        elif isinstance(item, list):
            pair, n_to_add, index, target_index = depth(item, k+1, n_to_add, index, target_index, b)
            new_l.append(pair)
        else:
            new_l.append(item)
            index += 1
    return new_l, n_to_add, index, target_index 

def modify_item(l, index, target_index, n_to_add):
    new_l = []
    for item in l:
        if isinstance(item, list):
            result, index = modify_item(item, index, target_index, n_to_add)
            new_l.append(result)
        else:
            if index == target_index:
                item += n_to_add
            new_l.append(item)
            index += 1

    return new_l, index

def explode_pair(pair):
    new_pair = [None] * 2
    if isinstance(pair[0], list) and isinstance(pair[1], list):
        new_pair[0] = 0
        pair[1][0] += pair[0][1]
        new_pair[1] = pair[1]
        return new_pair, pair[0][0], -1
    elif isinstance(pair[0], list):
        new_pair[0] = 0 
        new_pair[1] = pair[1] + pair[0][1]
        return new_pair, pair[0][0], -1
    elif isinstance(pair[1], list):
        new_pair[1] = 0 
        new_pair[0] = pair[0] + pair[1][0]
        return new_pair, pair[1][1], 1

def split(l, splitted=None):
    if splitted == None:
        splitted = False
    new_l = [] 
    for item in l:
        if isinstance(item, list):
            out, splitted = split(item, splitted)
            new_l.append(out)
        elif item >= 10 and not splitted:
            new_l.append([item//2, math.ceil(item/2)])
            splitted = True
        else: 
            new_l.append(item)
    return new_l, splitted

def count_magnitude(answer):
    value = []
    for e in answer:
        if isinstance(e, list):
            value.append(count_magnitude(e))
        else:
            value.append(e)
    return 3*value[0] + 2*value[1]

def read_data(inp):
    with open(inp) as f:
        l = []
        for line in f.readlines():
            l.append(ast.literal_eval(line.strip()))
    return l

if __name__ == '__main__':
    print(first(read_data('input')))
    print(second(read_data('input')))