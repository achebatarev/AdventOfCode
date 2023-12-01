import sys
from pprint import pprint
from collections import defaultdict, deque, Counter
import heapq
import math
from dataclasses import dataclass, field
import operator
import functools
import re 
from typing import List, Dict

try:
    FILE = sys.argv[1] 
except:
    FILE = 'test.in'

@dataclass
class Robot:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

    def __add__(self, other):
        return Robot(ore=self.ore + other.ore, clay=self.clay + other.clay, obsidian=self.obsidian + other.obsidian, geode=self.geode + other.geode)

    def __sub__(self, other):
        return Robot(ore=self.ore - other.ore, clay=self.clay - other.clay, obsidian=self.obsidian - other.obsidian, geode=self.geode - other.geode)

@dataclass    
class RobotCost(Robot):
    type: str = "costing"

@dataclass
class RobotStorage(Robot):
    pass

@dataclass
class Resources(Robot):
    pass

@dataclass
class Blueprint:
    n: int
    robots: List[RobotCost] =  field(default_factory=lambda: [])

def read_data(filename: str):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data

def time_to_gather(robots: Dict[str, int], need: Robot):
    t = 0
    for rock in robots:
        rock_needed = getattr(need, rock)
        n_robots = robots[rock]

        # check if we do not have a robot that provides a resource that we need
        # this check might even be irrelevant
        if rock_needed > 0 and n_robots == 0:
            return float('inf')

        if n_robots > 0:
            t = max(math.ceil(rock_needed / n_robots), t)

    return t

def resources_gathered(robots, t):
    print('Resources gathered', t, robots)
    return Resources(ore=robots['ore'] * t, clay=robots['clay'] * t, obsidian=robots['obsidian'] * t, geode=robots['geode'] * t)

def convert_key(robots):
    return f"{robots['ore']}, {robots['clay']}, {robots['obsidian']}, {robots['geode']}"

# Option 1
# For each minute, see if you can build a robot
# if you can, explore that brunch, otherwise continue
# We will need to keep track of resources and robots
# Option 2
# Try to answer the question, what if the next robot I build will be this one
# Problem:
# I do not produce results fast enough
# something that should happend on day 18 happens on day 19 

# Problem:
#    I build more geode robots than I should be capable of building
#       - I calculate how long it takes to gather resources to build a robot wrongly
#       - Calculating how much resources I have after building a robot is wrong 
#       - cost of robots is off
def find_geode(blueprint: Blueprint, limit: int) -> int:
    ans = 0
    robots = defaultdict(int)
    robots['ore'] = 1
    memo = {} 

    q = deque([(robots.copy(), Resources(), 0)])

    while q:
        for _ in range(len(q)):
            robots, resources, time_spent = q.popleft()

            total_geode = resources.geode + (robots['geode'] * (limit-time_spent))
            if total_geode >= ans:
                print(time_spent, total_geode, robots, resources)

            ans = max(ans, total_geode)

            for cost in blueprint.robots:
                need = cost - resources
                time_to_build = time_to_gather(robots, need) + 1
                total_time_spent = time_spent + time_to_build

                if total_time_spent >= limit:
                    continue

                new_robots = robots.copy()
                new_robots[cost.type] += 1

                if total_time_spent > memo.get(convert_key(new_robots), float('inf')):
                    continue

                memo[convert_key(new_robots)] = total_time_spent 

                new_resources = (resources + resources_gathered(robots, time_to_build)) - cost 
                print(resources, resources_gathered(robots, time_to_build), cost, new_resources)
                q.append((new_robots, new_resources, total_time_spent))

    return ans

def partA(data):
    k = 24 
    ans = 0
    for _, blueprint in enumerate(data):
        r = blueprint.n * find_geode(blueprint, k)
        print(r)
        ans += r

    return ans

    

def partB(data):
    pass

# PASS 
def parse_data(data):
    blueprints = []
    for blueprint in data: 
        a = list(map(int, re.findall(r'\d+', blueprint)))
        robots = []
        robots.append(RobotCost(type='ore', ore=a[1]))
        robots.append(RobotCost(type='clay', ore=a[2]))
        robots.append(RobotCost(type='obsidian', ore=a[3], clay=a[4]))
        robots.append(RobotCost(type='geode', clay=a[5], obsidian=a[6]))
        blueprints.append(Blueprint(a[0], robots))
    return blueprints 

if __name__ == '__main__':
    data = read_data(FILE)
    parsed_data = parse_data(data)
    print(partA(parsed_data))
    print(partB(parsed_data))
