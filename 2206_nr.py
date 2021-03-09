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

# 기존에 BFS 문제를 푸는 방식과 달리 table(즉 맵)과 visited(즉 이동 거리를 나타내는 리스트)를 구분해서 코딩했다는 점에서 많이 헷갈렸고 입력받을 때 잔실수가 있어서 해맸던 문제였다.
# 그리고 여태까지 해당 블럭의 위치로 이동거리를 표현하는데에서 2차원 배열을 사용하는 생각이 지배적이었지만 이 문제에는 블럭을 깼느냐 않깼느냐 같은 상태가 위치와 함께 3차원 배열을 사용했다는데에서 의미가 있다고 생각한다.

import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    queue = deque([((1, 1), 1)])  # ((x, y), 뚫었었는지 여부)
    visited = [[[0] * 2 for _ in range(M+1)] for _ in range(N+1)]
    visited[1][1][1] = 1
    while queue:
        tmp = queue.popleft()
        x, y, block = tmp[0][0], tmp[0][1], tmp[1]
        if x == N and y == M:
            return visited[x][y][block]
        for direction in range(4):
            nx = dx[direction] + x
            ny = dy[direction] + y
            if nx <= 0 or ny <= 0 or nx > N or ny > M:
                continue
            if table[nx][ny] == -1 and block == 1:
                visited[nx][ny][block-1] = visited[x][y][block] + 1
                queue.append(((nx, ny), 0))
            elif table[nx][ny] == 0 and visited[nx][ny][block] == 0:
                visited[nx][ny][block] = visited[x][y][block] + 1
                queue.append(((nx, ny), block))
    return -1

# input
N, M = map(int, input().split())
table = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(0, N):
    string = input()
    for j in range(0, M):
        if string[j] == '1':
            table[i+1][j+1] = -1
        else:
            table[i+1][j+1] = 0
# solution
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(bfs())

# 이런식으로 BFS를 진행하기 전에 따로 다른 맵을 만들고 시작하는 것은
# 이런 문제와 같이 미로의 벽 위치와 현재 위치의 이동거리를 혼동되지 않게 하는데 좋다..
# (미로의 벽 위치는 끝까지 바뀌면 안되는 곳이다.)