# 다익스트라, 힙 문제
# 한 정점에서 다른 모든 정점까지의 최소 거리를 모두 구하는 문제다.
# 또한 가중치가 붙은 그래프의 최소거리를 구하는 문제다.


import sys
import heapq
input = sys.stdin.readline

# input
heap = []
V, E = map(int, input().split())
K = int(input())
vertices = [[0 for j in range(V)] for i in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    vertices[u][v] = w
