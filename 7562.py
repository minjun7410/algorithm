# BFS 문제
# 체스 나이트의 이동으로 목적지까지 도착하는 '최소 거리'를 구하는 문제 -> BFS

import sys
input = sys.stdin.readline
from collections import deque

dx = [2, 2, 1, -1, -2, -2, 1, -1] # 나이트의 이동 범위를 표현 ( 총 8 개 )
dy = [1, -1, 2, 2, 1, -1, -2, -2] # <- 여기서 숫자 실수로 삽질함


def bfs():
    queue = deque()
    queue.append((start_y, start_x))
    knight_map[start_y][start_x] = 1
    while queue:
        y, x = queue.popleft()
        if y == dest_y and x == dest_x:
            break
        for direction in range(8):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx < 0 or ny < 0 or nx >= L or ny >= L:
                continue
            if knight_map[ny][nx] != 0:
                continue
            knight_map[ny][nx] = knight_map[y][x] + 1
            queue.append((ny, nx))
    return knight_map[dest_y][dest_x]


# input

for _ in range(int(input())):
    L = int(input())
    knight_map = [[0 for _ in range(L)] for _ in range(L)]
    start_y, start_x = map(int, input().split())
    dest_y, dest_x = map(int, input().split())
    # solution
    print(bfs() - 1)