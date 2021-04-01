# 다익스트라, 힙 문제
# 한 정점에서 다른 모든 정점까지의 최소 거리를 모두 구하는 문제다.
# 또한 가중치가 붙은 그래프의 최소거리를 구하는 문제다.

# 다익스트라 알고리즘은 모든 정점의 거리를 "갱신" 해가며 최소거리를 구하는 알고리즘이다.

import sys
import heapq
input = sys.stdin.readline

INF = 12345678
# solution


def dijkstra():
    heap = []  # 최소 힙
    visited = [INF for _ in range(V+1)]
    visited[K] = 0
    heapq.heappush(heap, (0, K))
    while heap:
        value, index = heapq.heappop(heap)
        for v, w in vertices[index]:
            tmp = visited[index] + w
            if visited[v] > tmp:
                visited[v] = tmp
                heapq.heappush(heap, (visited[v], v))
    return visited


def print_result(visited):
    for i in range(1, V+1):
        print(visited[i] if visited[i] != INF else "INF")


# input
V, E = map(int, input().split())
K = int(input())
vertices = [[] for i in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    vertices[u].append((v, w))
visited = dijkstra()
print_result(visited)

# 원리도 이해하기 어려웠고 코딩할 때도 많은 곤혹을 치렀다
# 처음으로 공간 복잡도를 해결하기 위해 각 간선의 정보를 저장할 때(38~39) 튜플을 이용해서 V^2 의 공간 복잡도를 피했다.
# 최소 힙을 응용하는 첫 문제였기 때문에 힙을 사용하는데 어리숙함도 있었고 힙의 중요성을 알게 된것 같음
