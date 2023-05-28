from pprint import pprint
from copy import deepcopy
from collections import deque
def first(arr):
    score = 0
    check = ((0,1), (1,0), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1))
    for w in range(100):
        found = False 
        for i,line in enumerate(arr):
            for j,e in enumerate(line):
                arr[i][j] += 1
        while True:
            for i,line in enumerate(arr):
                for j,e in enumerate(line):
                    if arr[i][j] > 9:
                        # increment all around
                        found = True
                        score += 1
                        arr[i][j] = 0
                        for r, c in check:
                            xr = j + r
                            yc = i + c
                            if xr >= 0 and xr < len(arr[0]) and yc >= 0 and yc < len(arr) and arr[yc][xr] != 0:
                                arr[yc][xr] += 1
            if not found:
                break
            found = False
    return score

def second(arr):
    check = ((0,1), (1,0), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1))
    step = 0
    goal = len(arr) * len(arr[0])
    n = 0
    while True:
        score = 0
        found = False 
        for i,line in enumerate(arr):
            for j,e in enumerate(line):
                arr[i][j] += 1

        while True:
            for i,line in enumerate(arr):
                for j,e in enumerate(line):
                    if arr[i][j] > 9:
                        # increment all around
                        found = True
                        score += 1
                        arr[i][j] = 0
                        for r, c in check:
                            xr = j + r
                            yc = i + c
                            if xr >= 0 and xr < len(arr[0]) and yc >= 0 and yc < len(arr) and arr[yc][xr] != 0:
                                arr[yc][xr] += 1

            if not found:
                break
            found = False
        step += 1
        if score == goal:
            #n += 1
            #print(n, w, score, goal)
            #pprint(arr)
            #if n > 3:
            break
    return step 
    
        

    #     for i,line in enumerate(arr):
    #         for j,e in enumerate(line):
    #             if e > 9 and (j, i) not in flashed:
    #                 stack.append((j, i))
    #                 while stack:
    #                     x, y = stack.pop()
    #                     visited.add((x, y))
    #                     if x >= 0 and x < len(arr[0]) and y >= 0 and y < len(arr):
    #                         arr[y][x] += 1
    #                         if arr[y][x] > 9:
    #                             flashed.add((x, y))
    #                             set_to_zero.append((x, y)) 
    #                             for r, c in check:
    #                                 # problem with visited is that sometimes I want to double count the same place
    #                                 if (x + r, y + c) not in visited:
    #                                     stack.append((x+r, y+c))
    #     for x, y in set_to_zero:
    #         arr[y][x] = 0
    #     if w < 10:
    #         print(w+1, j, i)
    #         pprint(arr)
    # return score

def change_lights(arr, x, y):
    if x < 0 or x >= len(arr[0]) or y < 0 or y >= len(arr):
        return 0
    arr[y][x] += 1
    if arr[y][x] >= 9:
        check = ((0,1), (1,0), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1))
        r = 1
        for i, j in check:
            r += change_lights(arr, x+i, y+j)
        arr[y][x] = 0
        return r
    elif arr[y][x] != 9:
        return 0
            


with open('input') as f:
    arr = []
    for line in f.readlines():
        arr.append(list(map(int,line.strip())))

#pprint(arr)
print(first(deepcopy(arr)))
print(second(deepcopy(arr)))

