from collections import defaultdict
ship = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
waypoint = {'N': 1, 'E': 10, 'S': 0, 'W': 0}
directions = ['N', 'E', 'S', 'W']

with open('input.txt') as f:
    for line in f.readlines():
        action = line[:1]
        value = int(line[1:])
        if action == 'F': 
            for direction in directions:
                ship[direction] += value * waypoint[direction]
        elif action in directions:
            waypoint[action] += value
        else:
            shift = value // 90
            if action == 'L':
                shift *= -1
            temp = []
            temp_way = defaultdict(int) 
            for i, key in enumerate(directions):
                temp.append((key, (i + shift) % len(directions)))
            for key, pos in temp:
                temp_way[directions[pos]] = waypoint[key]
            waypoint = temp_way

print(abs(ship['N'] - ship['S']) + abs(ship['E'] - ship['W']))


