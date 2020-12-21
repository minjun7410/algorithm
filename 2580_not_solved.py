from collections import deque
board = [[None for _ in range(9)] for _ in range(9)]
zero = []

for i in range(9):
    for j, value in enumerate(map(int, input().split())):
        board[i][j] = value
        if value == 0:
            zero.append((i, j))

zero_board = deque(zero[:])


def backtracking():
    while zero_board:
        tmp = zero_board.popleft()
        if check(tmp):
            continue
        else:
            zero_board.append(tmp)



def check(location):
    y = location[0]
    x = location[1]
    y_sum = len(list(filter(lambda i: i == 0, board[y][:])))
    x_sum = len(list(filter(lambda i: i == 0, board[:][x])))

    if y_sum == 1:
        need = list(filter(lambda i: i not in board[y][:], range(1, 10)))
        board[y][x] = need[0]
        return True
    elif x_sum == 1:
        need = list(filter(lambda i: i not in board[:][x], range(1, 10)))
        board[y][x] = need[0]
        return True
    
    div_board_y = (y // 3) * 3
    div_board_x = (x // 3) * 3

    div_sum = 0
    div = []
    for i in range(3):
        for j in range(3):
            div.append()
            if board[div_board_y + i][div_board_x + j] == 0:
                div_sum += 1
    if div_sum == 1:
        
    return False

backtracking()
for i in board:
    print(' '.join(map(str, i)))