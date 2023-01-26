from collections import deque
import sys

# 우 하 좌 상 (시계 방향)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
di = 0

input = sys.stdin.readline
N = int(input().rstrip())
K = int(input().rstrip())
table = [[0 for j in range(N)] for i in range(N)]

for _ in range(K):
    a, b = map(int, input().rstrip().split())
    table[a-1][b-1] = 1
table[0][0] = 2
snake_route = deque([(0,0)])

L = int(input().rstrip())
def game(di):
    result = 0
    P = 0
    for _ in range(L):
        X, C = input().rstrip().split()
        X = int(X)
        ny, nx = snake_route[-1]
        for i in range(P, X):
            result += 1
            ny += dy[di]
            nx += dx[di]
            if ny < 0 or nx < 0 or ny >= N or nx >= N: return result
            if table[ny][nx] == 2: return result
            elif table[ny][nx] == 0:
                # 꼬리 자르기
                y, x = snake_route.popleft()
                table[y][x] = 0
                # 이동
                table[ny][nx] = 2
                snake_route.append((ny, nx))
            else:
                table[ny][nx] = 2
                snake_route.append((ny, nx))
        di += 1 if C == 'D' else -1
        di = (di+4) % 4
        P = X
    while(1):
        result += 1
        ny += dy[di]
        nx += dx[di]
        if ny < 0 or nx < 0 or ny >= N or nx >= N: return result
        if table[ny][nx] == 2:
            return result
        elif table[ny][nx] == 0:
            # 꼬리 자르기
            y, x = snake_route.popleft()
            table[y][x] = 0
            # 이동
            table[ny][nx] = 2
            snake_route.append((ny, nx))
        else:
            table[ny][nx] = 2
            snake_route.append((ny, nx))
    return result
print(game(di))
