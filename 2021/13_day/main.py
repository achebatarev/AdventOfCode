from dataclasses import dataclass,field
from pprint import pprint, PrettyPrinter
@dataclass(unsafe_hash=True)
class Point:
    x:int =field(hash=True)
    y:int=field(hash=True)

    def transpose_horizontal(self, fold_line):
        diff = self.x - fold_line
        tr_x = fold_line - diff 
        tr_y = self.y
        return Point(tr_x, tr_y)

    def transpose_vertical(self, fold_line):
        diff = self.y - fold_line
        tr_x = self.x
        tr_y = fold_line - diff 
        return Point(tr_x, tr_y)

def first(points, fold):
    s = set()
    if fold[0] == 'x':
        for point in points:
            if point.x > fold[1]:
                s.add(point.transpose_horizontal(fold[1]))
            else:
                s.add(point)
    return len(s)

def second(points, folds):
    for fold in folds:
        s = set()
        if fold[0] == 'x':
            for point in points:
                if point.x > fold[1]:
                    s.add(point.transpose_horizontal(fold[1]))
                else:
                    s.add(point)
        elif fold[0] == 'y':
            for point in points:
                if point.y > fold[1]:
                    s.add(point.transpose_vertical(fold[1]))
                else:
                    s.add(point)
        points = s.copy() 
    visualize(s)


def visualize(points):
    # find max x, y and set them as length
    max_x = max(points, key=lambda x: x.x).x
    max_y = max(points, key=lambda x: x.y).y
    arr = [] 
    for _ in range(max_y+1):
        line = [' '] * (max_x + 1)
        arr.append(line)
    for point in points:
        arr[point.y][point.x] = '@'
    #pp = PrettyPrinter(width=500, compact=True)

    #pp.pprint(arr)
    for line in arr:
        for e in line:
            print(e, end='')
        print('\n')

points = []
folds = []
with open('input.txt') as f:
    for line in f.readlines():
        if not line.startswith('fold') and line != '\n':
            points.append(Point(*map(int,line.strip().split(','))))
        elif line.startswith('fold'):
            coord, loc = line.strip().split()[2].split('=')
            folds.append((coord, int(loc)))



#print(set(points))
#print(folds)
print(first(points, folds[0]))
second(points, folds)
