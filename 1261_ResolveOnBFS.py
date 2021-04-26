# 다익스트라 문제, BFS 문제
# 0-1 너비 우선 탐색으로 풀 수 있다는데 다익스트라로 풀고나서 나중에 분석할 것
# 현재 위치에서 상하좌우로 움직이는데 이동거리가 1일수도 있고 0일 수도 있기 때문에 가중치가 다른 그래프 문제로 다익스트라 문제이다.

import sys
import heapq
input = sys.stdin.readline
INF = 87654321

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# input
M, N = map(int, input().split())  # 가로 크기, 세로 크기
maze = [list(map(int, input().rstrip())) for _ in range(N)]
heap = [(0, 0, 0)]  # (이동거리, y, x)
visited = [[INF for _ in range(M)] for _ in range(N)]
visited[0][0] = 0
while heap:
    d, y, x = heapq.heappop(heap)
    for i in range(4):
        nx = dx[i] + x  # 이동할 장소의 x
        ny = dy[i] + y  # 이동할 장소의 y
        if nx < 0 or ny < 0 or nx >= M or ny >= N:
            continue
        nd = maze[ny][nx] + d  # 이동할 장소의 이동거리
        if nd >= visited[ny][nx]:
            continue
        heapq.heappush(heap, (nd, ny, nx))
        visited[ny][nx] = nd
print(visited[-1][-1])
