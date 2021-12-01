def binary_check(seat, upper_limit):
    low = 0
    high = upper_limit
    i = 0
    while i < len(seat):
        mid = low + ((high - low) // 2)
        if seat[i] == 'F' or seat[i] == 'L':
            high = mid
            i += 1
        elif seat[i] == 'B' or seat[i] == 'R':
            low = mid
            i += 1
    return high

seat_IDs = set() 
seat_ID = 0 
with open('input.txt') as f:
    for line in f.readlines():
        column = line.strip()[-3:]

        row = line.strip()[:-3]
        ID = (binary_check(row, 127) * 8) + binary_check(column, 7)
        seat_IDs.add(ID)
        seat_ID = max(seat_ID, ID)

for ID in seat_IDs:
    if ID+1 not in seat_IDs and ID+1 < seat_ID:
        print(ID+1)
