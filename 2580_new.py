board = [[None for _ in range(9)] for _ in range(9)]
location_lst = []
zero = 0
for i in range(9):
    for j, value in enumerate(map(int, input().split())):
        board[i][j] = value
        if value == 0:
            zero += 1
            location_lst.append((i, j))
fine = False


def backtracking(N):
    global fine
    if N == zero:
        fine = True
        return
    for i in range(1, 10):
        y = location_lst[N][0]
        x = location_lst[N][1]
        if check((y, x), i):
            board[y][x] = i
            backtracking(N + 1)
            if fine:
                return
            board[y][x] = 0
            
            
def check(location, number):
    y = location[0]
    x = location[1]
    for index in range(9):
        if number == board[y][index] or number == board[index][x]:
            return False

    div_board_y = y // 3 * 3
    div_board_x = x // 3 * 3

    for i in range(3):
        for j in range(3):
            if number == board[div_board_y + i][div_board_x + j]:
                return False

    return True


backtracking(0)

for i in board:
    print(' '.join(map(str, i)))

