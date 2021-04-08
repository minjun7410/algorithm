# 다익스트라 문제
# 문제를 이해하는데 오랜 시간이 걸렸다.
# 이 문제의 조건은 크게 두가지로 볼 수 있다.
# 1. 시작지점에서 목적지 후보에 최단 거리로 도착하는 후보군이 목적지다.
# 2. 이때 그 최단거리가 g와 h 사이를 지나야 한다.

import sys
import heapq

input = sys.stdin.readline
INF = 987654321


def dijkstra(start):  # 다익스트라 출발지점
    heap = [(start, 0)]  # (정점, 시작점까지 거리)
    distance = [INF for _ in range(n+1)]  # 시작점까지의 거리들을 리스트로 정리
    distance[start] = 0
    while heap:
        index, value = heapq.heappop(heap)
        for v, w in vertices[index]:
            tmp = value + w
            if distance[v] > tmp:
                distance[v] = tmp
                heapq.heappush(heap, (v, tmp))
    return distance


# input
for _ in range(int(input())):
    n, m, t = map(int, input().split())  # 교차로, 도로, 목적지 후보 개수
    s, g, h = map(int, input().split())  # 출발지, 거점 a, 거점 b
    vertices = [[] for _ in range(n+1)]  # 간선 리스트
    for _ in range(m):
        a, b, d = map(int, input().split())
        vertices[a].append((b, d))  # (노드, 거리)
        vertices[b].append((a, d))
    candidates = sorted([int(input()) for _ in range(t)])  # 후보군 리스트
    s_dij = dijkstra(s)
    g_dij = dijkstra(g)
    h_dij = dijkstra(h)
    g_h = g_dij[h]
    s_g = s_dij[g]
    s_h = s_dij[h]
    for candidate in candidates:
        shortest = s_dij[candidate]
        one = s_g + g_h + h_dij[candidate]
        two = s_h + g_h + g_dij[candidate]
        if shortest == min(one, two):
            print(candidate, end=' ')
    print()
    
