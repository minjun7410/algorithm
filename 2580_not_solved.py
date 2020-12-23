board = [[None for _ in range(9)] for _ in range(9)]
location_lst = []
zero = 0
for i in range(9):
    for j, value in enumerate(map(int, input().split())):
        board[i][j] = value
        if value == 0:
            zero += 1
fine = False


def backtracking():
    global fine
    if len(location_lst) == zero:
        fine = True
        return
    for i in range(9):
        for j in range(9):
            if not(board[i][j]):
                number = check((i, j))
                if (i, j) not in location_lst and number:
                    location_lst.append((i, j))
                    origin = board[i][j]
                    board[i][j] = number
                    backtracking()
                    if fine:
                        return
                    board[i][j] = origin
                    location_lst.pop()
    return


def check(location):
    y = location[0]
    x = location[1]
    lst = list(range(0, 10))
    
    for index in [i for i in range(9)]:
        lst[board[y][index]] = 0
        lst[board[index][x]] = 0

    div_board_y = (y // 3) * 3
    div_board_x = (x // 3) * 3

    for i in range(3):
        for j in range(3):
            lst[board[div_board_y + i][div_board_x + j]] = 0
    tmp = 0
    for i in range(10):
        if lst[i] != 0:
            tmp = i
            break
    return tmp


backtracking()

for i in board:
    print(' '.join(map(str, i)))

