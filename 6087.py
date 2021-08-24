# BFS 문제
# 꺾는 수를 그래프에 저장한다.
# 진행할 때 현재 노드가 다음 진행 노드보다 수가 적어야 함

# 너무 어렵게 풀었다
# visited를 왜 4개 방향 나눠서 관리해야하는지 이해가 안됬다.
# 하지만 지금까지 몇번 꺾었는지와 상관없이 방향에 따라 더 빨리 갈수 있기 때문
# 다른 알고리즘을 다루거나 미니 프로젝트 때문에 그래프 이론 문제를 푼지 오래되었는데 오랜만에 푸니까 어렵다

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
INF = 987654321
# 방향 [0, 1, 2, 3] = 동 서 남 북

# input
W, H = map(int, input().split())
table = [[] for _ in range(H)]
visited = [[[INF for _ in range(4)] for _ in range(W)] for _ in range(H)]
start, end = None, None
for i in range(H):
    for j, tmp in enumerate(list(input().rstrip())):
        table[i].append(tmp)
        if tmp == 'C':
            start = (i, j) if start == None else start
            end = (i, j) if start != None or end != None else end
queue = deque([])
for i in range(4):
    visited[start[0]][start[1]][i] = 0
    y = start[0] + dy[i]
    x = start[1] + dx[i]
    if y < 0 or x < 0 or y >= H or x >= W or table[y][x] == '*':    continue
    visited[y][x][i] = 0
    queue.append((y, x, i))
while queue:
    y, x, d = queue.popleft()
    if y == end[0] and x == end[1]:
        print(min(visited[y][x]))
        break
    for direction in range(4):
        ny = dy[direction] + y
        nx = dx[direction] + x
        if ny < 0 or nx < 0 or ny >= H or nx >= W or table[ny][nx] == '*': continue

        if d == direction:
            if visited[y][x][d] >= visited[ny][nx][direction]: continue
            visited[ny][nx][direction] = visited[y][x][d]
            queue.appendleft((ny, nx, direction))
        else:
            if visited[y][x][d] + 1 >= visited[ny][nx][direction]: continue
            visited[ny][nx][direction] = visited[y][x][d] + 1
            queue.append((ny, nx, direction))
