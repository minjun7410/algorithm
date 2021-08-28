# bfs 문제

# 타깃으로부터 가장 먼 거리를 가진 친구의 거리가 친밀도이다.
# N*N의 이차원 리스트를 만들어서 친구 거리를 저장한다.

# 알고리즘 분류를 안보고 푸는게 성장에 좋을 것 같아서 안보고 풀었다.
# 문제가 어떤 알고리즘으로 풀어야할지 쉽게 보여서 이번 문제는 힘을 들이지 않고 풀었던 것 같다.

import sys
from collections import deque
input = sys.stdin.readline
INF = 987654321
N = int(input())
edges = [[] for _ in range(N)]
visited = [[INF for _ in range(N)] for _ in range(N)]
for _ in range(INF):
    a, b = map(int, input().split())
    if a == -1 and b == -1: break
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

def bfs():
    for target in range(N):
        queue = deque([(target, 0)])
        while queue:
            node, value = queue.popleft()
            visited[target][node] = value
            for n in edges[node]:
                v = value + 1
                if visited[target][n] > v:
                    visited[target][n] = v
                    queue.append((n, v))
bfs()
min_value = INF
result = []
for i, arr in enumerate(visited):
    value = max(arr)
    if value == min_value:
        result.append(i)
    elif value < min_value:
        min_value = value
        result = [i]
print(min_value, len(result))
print(' '.join(map(lambda x: str(x+1), result)))