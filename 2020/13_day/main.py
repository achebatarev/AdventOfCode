import math
def first(goal, buses):
    l = [] 
    d = {}
    for Id in buses:
        try:
            Id = int(Id)
            n = goal / Id 
            # floor * n, roof * n
            d[Id] = math.ceil(n)*Id
        except:
            pass
    Id, least_n = sorted(d.items(), key=lambda x: x[1])[0]
    return Id * (least_n - goal)
def second(buses):
    t = 0
    info = []
    a = 1
    for i, bus in enumerate(buses): 
        if bus != 'x':
            # refine how congruence realtions are created
            info.append((int(bus), abs(int(bus)-i) if i != 0 else 0))
    current_lcm = 1
    # that solves a congruence relation with coprimes, need to find a proper congruence relation
    print(info)
    for i in range(1, len(info)):
        mod, r  = info[i-1]
        curr_mod, r2 = info[i]
        current_lcm = lcm(current_lcm, mod)
        gen = common(t, current_lcm)
        # two improvements:
        # 1.) get rid of large values
        # 2.) replace generation functions
        c = 0
        while c <= curr_mod:
            #print(t, curr_mod, t%curr_mod, r2, current_lcm)
            # there is always gonna be curr_mod steps at most
            if t % curr_mod == r2:
                break
            t = next(gen)
            c += 1
        print(t, curr_mod, t%curr_mod, r2, current_lcm)
        print('Step', c, ": Curr mod", curr_mod)

    return t
        




# if a and b coprimes no need for gcd
def lcm(a, b):
    #GCD = gcd(a, b)
    return (a * b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# create generating function that is going to yield a num in a sequence
def common(val, increment):
    while True:
        val += increment 
        yield val  



with open('input', 'r') as f:
    goal = int(f.readline().strip())
    buses = f.readline().strip().split(',')

print(first(goal, buses))
print(second(buses))
