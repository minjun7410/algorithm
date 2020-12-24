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
            if not(board[i][j]) and (i, j) not in location_lst:
                for number in range(1, 10):
                    if check((i, j), number):
                        location_lst.append((i, j))
                        board[i][j] = number
                        backtracking()
                        if fine:
                            return
                        board[i][j] = 0
                        location_lst.pop()
    return


def check(location, number):
    y = location[0]
    x = location[1]
    for index in [i for i in range(9)]:
        if number == board[y][index] or number == board[index][x]:
            return False

    div_board_y = y // 3 * 3
    div_board_x = x // 3 * 3

    for i in range(3):
        for j in range(3):
            if number == board[div_board_y + i][div_board_x + j]:
                return False

    return True


backtracking()

for i in board:
    print(' '.join(map(str, i)))

