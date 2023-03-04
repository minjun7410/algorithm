import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
queue = deque([])
table = [[] for i in range(N)]
for y in range(N):
    row = list(map(int, input().split()))
    for x, r in enumerate(row):

        if r == 1:
            table[y].append(r)
            queue.append((y, x))
        else:
            table[y].append(999)
dy = [1, 1, 1, 0, 0, -1, -1, -1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
while queue:
    y, x = queue.popleft()
    z = table[y][x]
    for d in range(8):
        ny = y + dy[d]
        nx = x + dx[d]
        if ny >= N or nx >= M or ny < 0 or nx < 0: continue
        nz = table[ny][nx]
        if z + 1 >= nz: continue
        table[ny][nx] = z + 1
        queue.append((ny, nx))
print(max(map(max, table))-1)