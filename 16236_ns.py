import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
move = 0
N = int(input())
table = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j, n in enumerate(map(int, input().split())):
        if n == 9:
            start_point = (i, j)
            continue
        table[i][j] = n
flag = True

def bfs(start_point, weight, move):
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque([start_point+tuple([move])])
    while queue:
        y, x, move_c = queue.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or nx < 0 or ny >= N or nx >= N or visited[ny][nx] == True: continue
            if table[ny][nx] > weight: continue
            elif table[ny][nx] == weight or table[ny][nx] == 0:
                visited[ny][nx] = True
                queue.append((ny, nx, move_c+1))
            else:
                visited[ny][nx] = True
                table[ny][nx] = 0
                return (ny, nx), move_c+1, True
    return (0, 0), move, False





weight = 2
eat = 0
while(flag):
    start_point, move, flag = bfs(start_point, weight, move)
    eat += 1
    if eat == weight:
        eat = 0
        weight += 1
print(move)


