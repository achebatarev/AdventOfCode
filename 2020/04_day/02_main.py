import string
def ecl(color):
    return color in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
def byr(date):
    return date.isdigit() and len(date) == 4 and int(date) >= 1920 and int(date) <= 2002
def iyr(year):
    return year.isdigit() and len(year) == 4 and int(year) >= 2010 and int(year) <= 2020 
def hgt(height):
    unit = height[-2:]
    height = int(height[:-2])
    return (height >= 150 and height <= 193) if unit == 'cm' else (height >= 59 and height <= 76)
def eyr(year):
    return year.isdigit() and len(year) == 4 and int(year) >= 2020 and int(year) <= 2030
def hcl(color):
    lowercase = string.ascii_lowercase
    digits = string.digits
    data = set(lowercase + digits)
    return color.startswith('#') and len(color) == 7 and all(c in data for c in color[1:])
def pid(num):
    return num.isdigit() and len(num) == 9

with open('input.txt') as f:
    r = 0
    d = {}
    features = {'ecl':ecl, 'pid':pid, 'eyr':eyr, 'hcl':hcl, 'byr':byr, 'iyr':iyr,'hgt':hgt}
    for line in f.readlines():
        if line == '\n':
            data = [1 for e in features if e in d]
            if len(data) == len(features):
                # print([features[feature](d[feature]) for feature in features])
                if all([features[feature](d[feature]) for feature in features]):
                    r += 1    
            d = {}
        else:
            dict2 = dict(field.split(':') for field in line.strip().split(" "))
            d.update(dict2) 

if len([1 for e in features if e in d]) == len(features) and all(features[feature](d[feature]) for feature in features):
    r += 1
print(r)
