# 이동 횟수를 구하는 문제이므로 BFS?
# BFS를 호출하는 횟수 -> 먼지 개수
# 만약 BFS에서 먼지를 찾지 못하면 -1 리턴하고 반복문 탈출
# 왠지 시간 초과가 날 것 같다. -> 적중

# 모든 노드 서로의 거리를 측정 (2차원 배열로)
# 시작 노드부터 모든 노드를 탐색하는데 거리도 측정.
# 가장 짧은
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(my, mx, y, x):
    visited = [[0 for _ in range(mx)] for _ in range(my)]
    visited[y][x] = 1
    queue = deque([(y, x, 0)])
    while queue:
        y, x, m = queue.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or nx < 0 or ny >= my or nx >= mx: continue  # out of range condition
            if room_map[ny][nx] == 'x' or visited[ny][nx] == 1: continue  # if robot faces wall, or robot went to which location again
            elif room_map[ny][nx] == '*':  # if robot faces dust

              # if robot do jobs as usual
            visited[ny][nx] = 1
            queue.append((ny, nx, m+1))
    return -1, (0, 0)
while(1):
    mx, my = map(int, input().split())  # row, column num
    if mx == 0 and my == 0: break  # 0, 0 -> exit
    result = 0
    nodes = []
    room_map = [[] for _ in range(my)]
    for i in range(my):
        for j, v in enumerate([_ for _ in input()]):
            if v == 'o': start = (i, j)
            if v == '*': nodes.append((i, j))
            room_map[i].append(v)

    nodes = [start] + nodes
    node_map = [[0 for _ in range(len(nodes))] for _ in range(len(nodes))]
    for y, x in nodes:
        bfs(my, mx, y, x)

