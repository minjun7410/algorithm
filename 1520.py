# 동적계획법, 백트랙킹 문제

M, N = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def backtracking(y, x):
    if y == M-1 and x == N-1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    ret = 0
    for direction in range(4):
        new_x = x + dx[direction]
        new_y = y + dy[direction]
        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
            continue
        if map_list[y][x] > map_list[new_y][new_x]:
            ret += backtracking(new_y, new_x)
    dp[y][x] = ret
    return ret


result = backtracking(0, 0)
print(result)