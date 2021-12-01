with open('input.txt') as f:
    r = 0
    d = {}
    features = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr','hgt']
    for line in f.readlines():
        if line == '\n':
            data = [1 for e in features if e in d]
            if len(data) == len(features):
                r += 1    
            d = {}
        else:
            dict2 = dict(field.split(':') for field in line.strip().split(" "))
            d.update(dict2) 

if len([1 for e in features if e in d]) == len(features):
    r += 1
            
print(r)

