from pprint import pprint

def first(boards, pos):
    fastest_board = (0,334121)
    for i, board in enumerate(boards):
        fastest_board = min(fastest_board, (i, board_bingo(board, pos)), key=lambda x: x[1])

    return get_score(boards[fastest_board[0]], pos, fastest_board[1]) 

def second(board, pos):
    fastest_board = (0,0)
    for i, board in enumerate(boards):
        fastest_board = max(fastest_board, (i, board_bingo(board, pos)), key=lambda x: x[1])

    return get_score(boards[fastest_board[0]], pos, fastest_board[1]) 


# search for numbers that have index larger than min_score
def get_score(board, pos, min_score):
    s = 0
    for line in board:
        for n in line:
            if pos[n] > min_score:
                s += int(n)
    # find n at pos min_score
    for key, value in pos.items():
        if value == min_score:
            return int(key) * s




# iterate over board two times
def board_bingo(board, pos):
    min_score = 3431
    #pprint(board)
    for line in board:
        max_score = 0 
        for e in line:
            max_score = max(max_score, pos[e])
        min_score = min(min_score, max_score)
    for x in range(len(board)):
        max_score = 0
        for y in range(len(board)):
            max_score = max(max_score, pos[board[y][x]])
        min_score = min(min_score, max_score)

    return min_score



positions = {} 
boards = []
with open('input', 'r') as f:
    line1 = f.readline().strip()
    for j, n in enumerate(line1.split(',')):
        positions[n] = j

    while True:
        line = f.readline()
        if not line:
            break
        board = []
        for _ in range(5):
            line = f.readline().strip()
            board.append(line.split())
        boards.append(board)
#print(positions)
#pprint(boards)
pprint(first(boards, positions))
print(second(boards, positions))



                
       


