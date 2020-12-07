from collections import defaultdict
def recursion(bag, d):
    if not d[bag[1]]:
        return bag[0]
    else:
        s = 0 
        for e in d[bag[1]]:
            s += recursion(e, d) 
        output = s * bag[0] + bag[0]
        return output 

d = defaultdict(list)
with open('input.txt') as f:
    for line in f.readlines():
        main_color = ''
        first = 0
        sentence = line.strip().split(' ')
        for i, word in enumerate(sentence):
            if 'bag' in word:
                color = ' '.join(sentence[i-2:i])
                if first == 0:
                    main_color = color
                    first = 1
                else:
                    if color != 'no other':
                        amount = int(sentence[i-3])
                        d[main_color].append((amount, color))
                    else:
                        d[main_color] = []
                        
print(recursion((1, 'shiny gold'), d)-1)
