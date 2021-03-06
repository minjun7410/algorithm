# BFS 
# 벽 하나를 부술 수 있는 가정하에 최단 거리를 구하는 문제 -> BFS
# 딱 한번 벽을 부술 수 있다.
# (1, 1)과 (N, M)에서 시작하는 BFS를 진행한다.
# 그 다음 모든 벽에 대해 해당 벽이 없을 때 이동거리를 구한다.
import sys
from collections import deque
import copy
input = sys.stdin.readline


def bfs(table):
    while queue:
        tmp = queue.popleft()
        for direction in range(4):
            nx = dx[direction] + tmp[0]
            ny = dy[direction] + tmp[1]
            if nx <= 0 or ny <= 0 or nx > N or ny > M or table[nx][ny] == -1:
                continue
            table[nx][ny] = table[tmp[0]][tmp[1]] + 1
            queue.append((nx, ny))

# input
N, M = map(int, input().split())
table = [[0 for _ in range(M+1)] for _ in range(N+1)]
walls = []
for i in range(N):
    string = input()
    for j in range(M):
        if string[j] == '1':
            table[i][j] = -1
            walls.append((i, j))
        else:
            table[i][j] = 0

table_copy = copy.deepcopy(table)

# solution
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
queue = deque([(1, 1)])
table[1][1] = 1
bfs(table)

min_value = 12345678

queue.append[(N, M)]
table_copy[-1][-1] = 1
bfs(table_copy)

for wall in walls:
    x = wall[0]
    y = wall[1]
    

    