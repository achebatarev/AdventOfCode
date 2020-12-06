a = 0  
with open('input.txt') as f:
    arr = []
    for line in f.readlines():
        if line != '\n':
            arr.append(line.strip())
        else:
            if arr:
                if len(arr) == 1:
                    a += len(arr[0])
                else:
                    for l in arr[0]:
                        t = 0
                        for i in range(1, len(arr)):
                            if l in arr[i]:
                                t += 1
                            if t == len(arr) - 1:
                                a += 1
            arr = []
print(a)

                        
