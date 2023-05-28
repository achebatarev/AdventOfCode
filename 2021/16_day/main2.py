from functools import reduce
from collections import deque
def main(msg):
    value =  0
    while len(msg) > 8:
        v_int, t_int = parse(msg)
    # then parse based if operator or literal
        if t_int != 4:
            value += parse_operator(msg, t_int)
        else:
            value += parse_literal(msg)
    return value 

# get version and type
def parse(msg):
    v = []
    t = []
    for _ in range(3):
        v.append(msg.popleft())
    for _ in range(3):
        t.append(msg.popleft())
    v_int = convert_bin_to_int(''.join(v))
    t_int = convert_bin_to_int(''.join(t))
    return v_int, t_int


def convert_bin_to_int(binary:str):
    digit = 0
    for i, bit in enumerate(binary):
        if bit == '1':
            digit += 2**(len(binary)-i-1)
    return digit
    
def parse_operator(msg, type_version:int):
    lt = msg.popleft()
    operator_values = []
    if lt == '0':
        tl = []
        for _ in range(15):
            tl.append(msg.popleft())
        total_length = convert_bin_to_int(''.join(tl))
        current_length = len(msg)
        while current_length - len(msg) < total_length:
            v_int, t_int = parse(msg)
            if t_int != 4:
                value = parse_operator(msg, t_int)
            else:
               value = parse_literal(msg)
            operator_values.append(value)
    elif lt == '1':
        p = []
        for _ in range(11):
            p.append(msg.popleft())
        packet_num = convert_bin_to_int(''.join(p))
        for _ in range(packet_num):
            v_int, t_int = parse(msg)
            if t_int != 4:
                value = parse_operator(msg, t_int)
            else:
                value = parse_literal(msg)
            operator_values.append(value)
    # depending on a version number of this operator packet perform certain actions on operator values
    print(operator_values, type_version)
    return evaluate_value(operator_values, type_version)

def evaluate_value(values, version):
    if version == 0:
        return sum(values)
    elif version == 1:
        return reduce(lambda x, y: x*y, values)
    elif version == 2:
        return min(values)
    elif version == 3:
        return max(values)
    elif version == 5:
        return 1 if values[0] > values[1] else 0
    elif version == 6:
        return 1 if values[1] > values[0] else 0
    elif version == 7:
        return 1 if values[0] == values[1] else 0

    

def parse_literal(msg):
    start = 1
    final = []
    while start != '0':
        start = msg.popleft()
        for _ in range(4):
            e = msg.popleft()
            final.append(e)
    return convert_bin_to_int(''.join(final))

d = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

with open('input') as f:
    line = f.readline().strip()
out = []
for h in line:
    out.append(d[h])

message = ''.join(out)
#assert main(deque(message)) == 54
print(main(deque(message)))


