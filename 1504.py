# 다익스트라 문제
# 가중치가 있는 그래프의 최단거리를 구함 -> 다익스트라 알고리즘
# 특정 정점 a, b를 반드시 거쳐야하는 조건이 있다.

import sys
import heapq
input = sys.stdin.readline

INF = 12345678

# input
N, E = map(int, input().split())
vertices = {i:[] for i in range(1, N+1)}
for _ in range(E):
    a, b, c = map(int, input().split())
    vertices[a].append((b, c))
    vertices[b].append((a, c))
v1, v2 = map(int, input().split())

def dijkstra(v1, v2):
    heap = []
    heapq.heappush(heap, (v1, 0))
    distance = [INF for _ in range(N+1)]
    distance[v1] = 0
    while heap:
        index, value = heapq.heappop(heap)
        for v, d in vertices[index]:
            tmp = value + d
            if distance[v] > tmp:
                distance[v] = tmp
                heapq.heappush(heap, (v, tmp))
    return distance[1], distance[v2], distance[N]
start_1, mid_1, end_1 = dijkstra(v1, v2)
start_2, mid_2, end_2 = dijkstra(v2, v1)
if end_1 == INF or end_2 == INF:
    print(-1)
else:
    print(min(start_1 + mid_1 + end_2, start_2 + mid_2 + end_1))
    
# 시작과 끝 정점에서 다익스트라로 각 지나야하는 정점을 구하는 것이 아닌
# 각 지나야하는 정점에서 시작과 끝 정점 + 서로의 지나야하는 정점을 구하는 방법으로 하니 AC
# 아직 다익스트라가 익숙하지 않아서 이전에 푼 문제의 소스코드를 보면서 코딩했다.