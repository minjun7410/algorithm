# 다익스트라 문제
# N명의 학생 중에서 X로부터 가장 거리가 먼 학생을 구하는 문제.
# 한 노드로 부터 모든 노드의 최단거리를 구하는 문제 -> 다익스트라

import sys
import heapq
input = sys.stdin.readline
INF = 87654321

N, M, X = map(int, input().split())
students = [[] for _ in range(N+1)]
students_r = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, time = map(int, input().split())
    students[end].append((start, time))
    students_r[start].append((end, time))
def dijkstra(X, student):
    distances = [0] + [INF for _ in range(N)]
    distances[X] = 0
    heap = []
    heapq.heappush(heap, (0, X))
    while heap:
        distance, present = heapq.heappop(heap)
        if distances[present] < distance:   continue
        # 위의 구문의 필요한지 의심했었는데 예를들어 증명하자면

        # 1. 이전에 특정 노드를 조사할 당시 거리가 5였고 당시로선 가장 작은 거리였다
        # 2. 하지만 나중에 다른 노드에서 그 특정 노드를 조사했을 때 거리가 3이었고 갱신했다면
        # 3. 나중에 거리가 5였던 노드의 차례가 돌아왔을 때 이미 다른 최소거리를 구한 상태이므로 무시해도 좋다.

        for node, time in student[present]:
            if distances[node] > distance + time:
                distances[node] = distance + time
                heapq.heappush(heap, (distance + time, node))
    return distances
result = 0
for going, coming in zip(dijkstra(X, students), dijkstra(X, students_r)):
    result = max(result, going + coming)
print(result)
