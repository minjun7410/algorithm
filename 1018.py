def check_board(n, m, shape1, shape2):
    global board
    tmp = shape1
    sums = 0
    for i in range(8):
        for j in range(8):
            if board[n + i][m + j] != tmp:
                sums += 1
            tmp = shape2 if tmp == shape1 else shape1
        tmp = shape2 if tmp == shape1 else shape1
    return sums
N, M = map(int, input().split())
board = [[' ' for _ in range(M)] for _ in range(N)]
for i in range(N):
    board[i] = list(input())
least = 64
for i in range(N-8 + 1):
    for j in range(M-8 + 1):
        sums = check_board(i, j, 'B', 'W')
        if sums < least:
            least = sums
        sums = check_board(i, j, 'W', 'B')
        if sums < least:
            least = sums
print(least)