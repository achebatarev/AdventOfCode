from collections import defaultdict
from collections import deque
d = defaultdict(list)
with open('input.txt') as f:
    for line in f.readlines():
        sentence = line.strip().split(' ' )
        first = 0
        main_color = ''
        for i, word in enumerate(sentence): 
            if 'bag' in word:
                color = ' '.join(sentence[i-2:i])
                if first == 0:
                    main_color = color
                    first = 1
                else:
                    d[main_color].append(color)
bag = 'shiny gold'
visited = set() 
a = -1
q = deque()
q.append(bag)
while q:
    bag = q.popleft()
    for key, item in d.items():
        if bag in item and key not in visited:
            q.append(key)
            visited.add(key)
    a += 1
print(a)

                
