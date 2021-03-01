# BFS 문제
# 7576의 3차원 버전
# 3차원이기 때문에 입력과 자료구조에 신경을 써야할것 같다.

import sys
from collections import deque
input = sys.stdin.readline

# input

M, N, H = map(int, input().split())
table = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# solution

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

queue = deque([])

for h in range(H):
    for i in range(N):
        for j in range(M):
            if table[h][i][j] == 1:
                queue.append((h, i, j))

while queue:
    temp = queue.popleft()
    for direction in range(6):
        nh = dh[direction] + temp[0]
        ny = dy[direction] + temp[1]
        nx = dx[direction] + temp[2]
        if nh < 0 or ny < 0 or nx < 0 or nh >= H or ny >= N or nx >= M:
            continue
        if table[nh][ny][nx] != 0:
            continue
        queue.append((nh, ny, nx))
        table[nh][ny][nx] = table[temp[0]][temp[1]][temp[2]] + 1

def checking_zero():
    max_value = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if table[h][i][j] == 0:
                    return -1
                max_value = max(max_value, table[h][i][j])
    return max_value - 1

print(checking_zero())