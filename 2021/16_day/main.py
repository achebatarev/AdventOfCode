from collections import deque
def first(msg):
    a = 0
    while len(msg) > 8:
# get 6 first to identify v and t
        v_int, t_int = parse(msg)
        a += v_int
    # then parse based if operator or literal
        if t_int != 4:
            a += parse_operator(msg, v_int)
        else:
            parse_literal(msg)
    return a


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
    
def parse_operator(msg, version):
    lt = msg.popleft()
    operator_values = []
    a = 0
    if lt == '0':
        tl = []
        for _ in range(15):
            tl.append(msg.popleft())
        total_length = convert_bin_to_int(''.join(tl))
        current_length = len(msg)
        while current_length - len(msg) < total_length:
            v_int, t_int = parse(msg)
            a += v_int
            if t_int != 4:
                a += parse_operator(msg,v_int)
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
            a += v_int
            if t_int != 4:
                a += parse_operator(msg, v_int)
            else:
                value = parse_literal(msg)

    return a

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

print(first(deque(message)))


