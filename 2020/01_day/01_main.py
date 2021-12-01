with open('input.txt') as f:
    target = 2020
    s = set()
    for line in f.readlines():
        num = int(line.strip())
        val = target - num
        if val in s:
            print(num, val, val * num)
        s.add(num)

        
