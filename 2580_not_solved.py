from collections import deque
board = [[None for _ in range(9)] for _ in range(9)]
zero = []

for i in range(9):
    for j, value in enumerate(map(int, input().split())):
        board[i][j] = value
        if value == 0:
            zero.append((i, j))
# zero_lst는 진행 상태이다.
zero_lst = []


def backtracking():
    if len(zero_lst) == len(zero):
        
        return
    for i in zero:
        if i not in zero_lst and check(i):
            zero_lst.append(i)
            backtracking()
            zero_lst.pop()



def check(location):
    y = location[0]
    x = location[1]
    # y_lst, x_lst는 해당 리스트에서 필요한 요소들이다
    
    y_sum = 0
    y_lst = [i for i in range(1, 10)]
    for i in range(9):
        if board[y][i] == 0:
            y_sum += 1
        else:
            y_lst.remove(board[y][i])
            
    
    x_sum = 0
    x_lst = [i for i in range(1, 10)]
    for i in range(9):
        if board[i][x] == 0:
            x_sum += 1
        else:
            x_lst.remove(board[i][x])
            
    
    if y_sum == 1:
        board[y][x] = y_lst[0]
        return True
    if x_sum == 1:
        board[y][x] = x_lst[0]
        return True
    
    div_board_y = (y // 3) * 3
    div_board_x = (x // 3) * 3

    div_sum = 0
    div = [i for i in range(1, 10)]
    for i in range(3):
        for j in range(3):
            if board[div_board_y + i][div_board_x + j] == 0:
                div_sum += 1
            else:
                div.remove(board[div_board_y + i][div_board_x + j])
    if div_sum == 1:
        board[y][x] = div[0]
        return True
    return False

backtracking()
for i in board:
    print(' '.join(map(str, i)))