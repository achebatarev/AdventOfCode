#PROBLEM DETAILS
#---------------------------------------------------------------------------------------
# scanner picks up beacons that are 1000 untis away from them
# beacon position is relative to the scanner
# scanners do not know their own position, determine that
# there are at least 12 beacons that both scanners detect in the overlap between them
# each scanner could be rotated 90 inf times around x, y, and z
# does all pairs of scanners has at least 12 beacons overlapped, or only some pairs?
#---------------------------------------------------------------------------------------
#POSSIBLE SOLUTIONS
#---------------------------------------------------------------------------------------
#1. create overlapping function that finds overlaps
#2. rotate each scanner prespective
#3. find overlapping beacons
#---------------------------------------------------------------------------------------

from dataclasses import dataclass
from pprint import pprint
from copy import deepcopy

@dataclass
class Pos:
    x:int
    y:int
    z:int

    def subtract(self, point):
        return Pos(self.x - point.x, self.y - point.y, self.z - point.z)

    def add(self, point):
        return Pos(self.x + point.x, self.y + point.y, self.z + point.z)



# 1. assume scanner 1 is located at 0, 0, 0 pick point from scan1
# 2. pick point from scan2 
# 3. assume scanner 2 is located at the location where the point picked is true
# 4. Then plot all of the scan2 points on a graph asuuming it is positioned at the pos that would make previous one true 
# 5. See how many points will overlap
# 6. Repeat until run out of scan 1 points and save the result
#TODO: Speed this up
def beacon_overlapping(scan1, scan2, goal):
    # I need to return the postion of scanner 2 relative to scanner 1
    total_overlap = 0
    a = 0
    for point1 in scan1:
        for point2 in scan2:
            local_overlap = 0
            scan2_position = point1.subtract(point2)
            #get location of scan2 beacons relative to scan1
            relative_to_scan1 = []
            for position in scan2:
                relative_to_scan1.append(position.add(scan2_position))
            # now find overlaps in scan1
            for pos in relative_to_scan1:
                if pos in scan1:
                    local_overlap += 1
            total_overlap = max(local_overlap, total_overlap)
            if total_overlap == local_overlap and total_overlap >= goal:
                print(total_overlap)
                a = scan2_position
                print(a)
    return a

    #1, 3



def get_all_prespectives(pos: Pos):
    prespectives = []
    # positive or negative and 4 directions as up
    # 4 directions as up: z = x,-x,y,-y
    prespectives = find_permutations(list(deepcopy(pos.__dict__).values())+[4])
    #print(find_neg_pos_permutations(list(deepcopy(pos.__dict__).values())))
    return len(prespectives), prespectives

def find_neg_pos_permutations(positions):
    if len(positions) == 1:
        return [[positions[0]*-1], [positions[0]]]
    loc = len(positions) - 1
    first = find_neg_pos_permutations(positions[loc:])  
    second = find_neg_pos_permutations(positions[:loc])
    new_l = []
    for e in first:
        for i in second:
            new_l.append(i+e)
    return new_l
            

def find_permutations(positions):
    if len(positions) == 1:
        return [positions]
    new_l = []
    for i in range(len(positions)):
        first = positions[i]
        second = find_permutations(positions[:i] + positions[i+1:])
        for permutation in second:
            new_l.append([first] + permutation)
    return new_l







def read_data(inp):
    scanners = []
    with open(inp) as f:
        while True:
            line = f.readline()
            if not line:
                scanners.append(scanner)
                break
            if line.startswith('---'):
                scanner = []
            elif line != '\n':
                scanner.append(Pos(*map(int,line.strip().split(','))))
            else:
                scanners.append(scanner)
    return scanners

if __name__ == '__main__':
    pprint(read_data('test'))
    pprint(get_all_prespectives(Pos(1,2,3)))





    
