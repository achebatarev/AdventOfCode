position = {'E': 0, 'S': 0, 'W': 0, 'N': 0}
current = 'E'
directions = ('E', 'S', 'W', 'N')
with open('input.txt') as f:
    for line in f.readlines():
        action = line[:1]
        value = int(line.strip()[1:])
        if action in position:
            position[action] += value
        elif action == 'F':
            position[current] += value
        elif action in ('R','L'):
            start = directions.index(current)
            move = value // 90
            if action == 'L':
                move *= -1
            current = directions[(start + move) % len(directions)]

print(abs(position['E'] - position['W']) + abs(position['S'] - position['N']))
