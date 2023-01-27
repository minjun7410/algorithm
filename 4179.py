from collections import deque
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

R, C = map(int, input().split())

table = [[] for _ in range(R)]
manY, manX, fireY, fireX = 0, 0, 0, 0
visited = [[False for i in range(C)] for j in range(R)]
queue = deque([])
for i in range(R):
    for j, t in enumerate(input()):
        table[i].append(t)
        if t == 'J':
            queue.append((i, j, 0, True))
            visited[i][j] = True
        elif t == 'F':
            queue.appendleft((i, j, -1, False))
            visited[i][j] = True

result = 0
while(queue):
    py, px, point, isMan = queue.popleft()
    for i in range(4):
        ny, nx = py + dy[i], px + dx[i]
        if isMan:
            if ny < 0 or nx < 0 or ny >= R or nx >= C:
                result = point+1
                queue = []
                break
            if not(visited[ny][nx]) and table[ny][nx] != '#':
                visited[ny][nx] = True
                queue.append((ny, nx, point+1, True))
        else:
            if ny < 0 or nx < 0 or ny >= R or nx >= C:
                continue
            if not(visited[ny][nx]) and table[ny][nx] != '#':
                visited[ny][nx] = True
                queue.append((ny, nx, -1, False))
print(result if result != 0 else "IMPOSSIBLE")
