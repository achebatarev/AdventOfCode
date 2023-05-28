from dataclasses import dataclass

def first(goal_x, goal_y):
    min_y = min(goal_y)
    x = 0
    for i in range(max(goal_x),0, -1):
        #print(i, (i*(i+1))//2)
        if (i * (i+1)) // 2 in goal_x:
            x = i
            break
    high = (min_y*-1) -1
    velocity = Velocity(x=x, y=high)
    if one_launch(velocity, goal_x, goal_y):
        return (high * (high + 1)) // 2


def second(goal_x, goal_y):
    max_x = max(goal_x)
    min_y = min(goal_y)
    c = 0
    for x in range(max_x+1):
        for y in range(min_y, min_y*-1):
            velocity = Velocity(x=x, y=y)
            if one_launch(velocity, goal_x, goal_y):
                c += 1
    return c


def one_launch(velocity, goal_x, goal_y):
    min_y = min(goal_y)
    pos = Pos(x=0, y=0)
    #print(pos, velocity)
    while True:
        pos, velocity = step(pos, velocity)
        #print(pos, velocity)
        if pos.x in goal_x and pos.y in goal_y:
            return True
        elif pos.y < min_y:
            return False

def step(pos, velocity):
    new_pos = Pos(x=pos.x+velocity.x, y=pos.y+velocity.y)
    new_velocity_x = velocity.x 
    if new_velocity_x > 0:
        new_velocity_x -= 1
    elif new_velocity_x < 0:
        new_velocity_x += 1

    new_velocity = Velocity(x=new_velocity_x, y=velocity.y-1)
    return new_pos, new_velocity

@dataclass
class Pos:
    x: int
    y: int

@dataclass
class Velocity:
    x: int
    y: int

with open('input') as f:
    line = f.readline()
    x = line.split()[2]
    y = line.split()[3]
    x = x.split('=')[1][:-1]
    y = y.split('=')[1]
    x = list(map(int, x.split('..')))
    y = list(map(int, y.split('..')))
    range_x = set(range(x[0], x[1]+1))
    range_y = set(range(y[0], y[1]+1))

print(first(range_x, range_y))
print(second(range_x, range_y))