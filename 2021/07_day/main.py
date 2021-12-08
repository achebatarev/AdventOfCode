def first(inp):
    # naive approach, for each position calcluate amount of fuel it would take and then choose min
    s = list(range(min(inp), max(inp)+1))  
    least_fuel = 343241321 
    for e in s:
        fuel = 0
        for x in inp:
            diff = abs(e-x)
            fuel += diff 
        least_fuel = min(fuel, least_fuel)
    return least_fuel

def second(inp):
    # naive approach, for each position calcluate amount of fuel it would take and then choose min
    s = list(range(min(inp), max(inp)+1))  
    least_fuel = 343241321 
    for e in s:
        fuel = 0
        for x in inp:
            diff = abs(e-x)
            fuel += (diff * (diff + 1)) // 2
        least_fuel = min(fuel, least_fuel)
    return least_fuel

with open('input', 'r') as f:
    inp = list(map(int, f.readline().split(',')))

print(first(inp))
print(second(inp))
