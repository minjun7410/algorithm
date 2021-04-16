# 다익스트라 문제
# 출발 지점에서 도착지점까지 음수없는 경로로 최단거리를 구하는 문제 -> 다익스트라
# 다익스트라 알고리즘의 기본 문제
# 같은 출발지점, 도착지점에 거리만 다를 수 있으므로 vertices 리스트 안에 튜플에 도착지점과 거리를 입력하는 구조를 만들어야한다.
# ex 1 2 10
#    1 2 20

import sys
import heapq

input = sys.stdin.readline

INF = 987654321

# input
N = int(input())
M = int(input())
vertices = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    vertices[a].append((b, c))  # (도착지점, 거리)
start, end = map(int, input().split())

heap = [(start, 0)]
distances = [INF for _ in range(N+1)]
distances[start] = 0
while heap:
    index, value = heapq.heappop(heap)
    for v, w in vertices[index]:
        tmp = w + value
        if tmp < distances[v]:
            distances[v] = tmp
            heapq.heappush(heap, (v, tmp))
print(distances[end])