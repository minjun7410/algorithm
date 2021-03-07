# BFS 
# 벽 하나를 부술 수 있는 가정하에 최단 거리를 구하는 문제 -> BFS
# 딱 한번 벽을 부술 수 있다.
# (1, 1)과 (N, M)에서 시작하는 BFS를 진행한다.
# 그 다음 모든 벽에 대해 해당 벽이 없을 때 이동거리를 구한다.
# ------------------------------------------------------
# 더 효율적인 방법으로
# 덱에 넣을 인자를 (x, y)만 표현하지 않고 ((x, y), 뚫었었는지 여부) 이렇게 넣으면
# 도착지점은 최단 시간이 되어 있을 것  (만약 0이라면 도착 X)
# 주의 사항으로 벽을 뚫었을 때의 2차원 리스트와 뚫지 않았을 때 2차원 리스트를 구분해야한다. (3/7)
import sys
from collections import deque
import copy
input = sys.stdin.readline


def bfs(table):
    while queue:
        tmp = queue.popleft()
        x, y, block = tmp[0][0], tmp[0][1], tmp[1]
        for direction in range(4):
            nx = dx[direction] + x
            ny = dy[direction] + y
            if nx <= 0 or ny <= 0 or nx > N or ny > M:
                continue
            elif table[nx][ny] == -1 and block == 1:
                table[nx][ny] = table[x][y] + 1
                queue.append(((nx, ny), 0))
                continue
            elif table[nx][ny] != 0:
                continue
            table[nx][ny] = table[x][y] + 1
            queue.append(((nx, ny), block))

# input
N, M = map(int, input().split())
table = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(N):
    string = input()
    for j in range(M):
        if string[j] == '1':
            table[i][j] = -1
        else:
            table[i][j] = 0

# solution
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
queue = deque([((1, 1), 1)])  # ((x, y), 뚫었었는지 여부)
table[1][1] = 1
bfs(table)

print(table)


    

    