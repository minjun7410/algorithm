# bfs 문제
# 큐에 (x, y,  말 횟수)의 정보를 넣는다.
# 말 횟수를 다 썼을 땐 상하좌우 움직임만 표현한다.
# 2206문제와 같이 table과 visited를 분리하여 관리했고
# x, y와 함께 '말 횟수'라는 상태를 추가하여 3차원으로 visited 배열과 큐에 들어가는 튜플을 관리했다.

# BFS를 까먹을 까봐 찾아서 풀었더니 살짝 버겁다.
# BFS는 중요한 알고리즘이니 꾸준히 풀도록 하자.

import sys
from collections import deque
input = sys.stdin.readline
INF = 987654321

dx = [1, 0, -1, 0, 2, 2, 1, -1, -2, -2, -1, 1]
dy = [0, 1, 0, -1, -1, 1, 2, 2, 1, -1, -2, -2]
# solution
def bfs(visited):
    queue = deque([])
    queue.append((0, 0, 0))
    visited[0][0][0] = 0
    while queue:
        x, y, k = queue.popleft()
        d = 12 if k < K else 4
        for direction in range(d):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx < 0 or ny < 0 or nx >= H or ny >= W or table[nx][ny] == 1:  continue
            if direction < 4:
                if visited[nx][ny][k] > visited[x][y][k] + 1:
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    queue.append((nx, ny, k))
            else:
                if visited[nx][ny][k+1] > visited[x][y][k] + 1:
                    visited[nx][ny][k+1] = visited[x][y][k] + 1
                    queue.append((nx, ny, k+1))
    return

#input
K = int(input())  # K: 말 횟수
W, H = map(int, input().split())  # W: 가로길이 H: 세로길이
table = [list(map(int, input().split())) for _ in range(H)]  # table: 격자판
visited = [[[INF for _ in range(K+1)] for _ in range(W)] for _ in range(H)]  # vistied[x][y][k]: # x, y에서 k번 말 이동을 한 이동거리
bfs(visited)

# print
result = min(visited[-1][-1])
if result == INF:
  print(-1)
else:
  print(result)