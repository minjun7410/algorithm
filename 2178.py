# BFS 문제
# 미로 탈출의 "최단" 거리를 구하는 문제이기 때문에 (간선 1개당 거리 1증가)
# 1. table[0][0] 부터 상하좌우 검사해서 1인 노드만 덱에 넣는다.
# 2. 이미 조사한 노드는 거리로 방문 표시를 한다.
# 3. table[-1][-1] print
# 덱을 이용해서 head에 노드를 추가시키는 방식으로 진행

from collections import deque
import sys
input = sys.stdin.readline
#input
N, M = map(int, input().split())
table = []
for _ in range(N):
    table.append(list(map(int, input().rstrip())))

# answer

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

queue = deque([(0, 0)]) # 0, 0 부터 진행
while queue:
    tmp = queue.popleft()
    distance = table[tmp[0]][tmp[1]]
    for direction in range(4):
        nx = dx[direction] + tmp[0]
        ny = dy[direction] + tmp[1]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        elif table[nx][ny] != 1:
            continue
        else:
            table[nx][ny] = table[tmp[0]][tmp[1]] + 1
            queue.append((nx, ny))
print(table[-1][-1])
            
    