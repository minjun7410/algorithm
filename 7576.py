# BFS 문제
# 모든 토마토를 익히기 위한 "최단" 시간을 구하는 문제 -> BFS 가능성
# 1. 익은 토마토가 들어있는 모든 위치를 조사후 덱에 넣기
# 2. 현재 토마토의 위치에 상하좌우 중 0인 토마토에 시간+1
# 3. 시간을 매기는데 가장 큰 숫자를 따로 저장한다.
# 4. 토마토가 들어있지 않은 칸에 둘러싸인 토마토가 있을 수 있으니 마지막에 모든 토마토를 조사한다.(처음에 조사해도 될듯)

import sys
from collections import deque

input = sys.stdin.readline

# input

M, N = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# answer
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque([])

for i in range(N):
    for j in range(M):
        if table[i][j] == 1:
            queue.append((i, j))

while queue:
    tmp = queue.popleft()
    for direction in range(4):
        nx = dx[direction] + tmp[0]
        ny = dy[direction] + tmp[1]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if table[nx][ny] != 0:
            continue
        table[nx][ny] = table[tmp[0]][tmp[1]] + 1
        queue.append((nx, ny))

def check_zero():
    max_value = 0
    for i in range(N):
        for j in range(M):
            if table[i][j] == 0:
                return -1
            else:
                max_value = max(max_value, table[i][j])
    return max_value - 1
print(check_zero())