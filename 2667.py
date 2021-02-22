# BFS DFS
# 반복문으로 모든 블럭을 조사, 0이면 continue 1이면 함수 실행, -1(방문)이면 그대로 진행
# 너비 우선 탐색으로 이어진 모든 블럭에 방문표시를 한 후 덱에 아무 블럭이 남아있지 않은 경우 따로 카운트해놓은 수를 프린트
from collections import deque
# input

graph = []
N = int(input())
for _ in range(N):
    graph.append(list(map(int, input()))) # <- 입력을 보완
# answer
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

res = []

def bfs(i, j):
    result = 0
    queue = deque([(i, j)])
    graph[i][j] = -1
    while queue:
        tmp = queue.popleft()
        result += 1
        for direction in range(4):
            ni = tmp[0] + dx[direction]
            nj = tmp[1] + dy[direction]
            if nj < 0 or ni < 0 or ni >= N or nj >= N:
                continue
            if graph[ni][nj] != 1:
                continue
            queue.append((ni, nj))
            graph[ni][nj] = -1
    res.append(result)
    return
        

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i, j)

# print
print(len(res))
for value in sorted(res):
    print(value)