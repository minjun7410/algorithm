# BFS 문제
# 이 문제는 점 N가 K까지 갈 때 필요한 "최소" 비용을 구하는 문제 -> BFS
# 다른 문제와는 다르게 그래프가 1차원이다.
# 동적계획법으로 풀 수 있을 듯 ( 속도는 이전에 방문한 노드가 동적계획법이 더 많으므로 BFS가 빠를 것 같다. )
import sys
from collections import deque
input = sys.stdin.readline

# input
N, K = map(int, input().split())

# solution
max_value = max(N, K)
graph = [0 for _ in range(max_value + 1)]
graph[N] = 0
queue = deque([N])
while queue:
    tmp = queue.popleft()
    for value in [tmp-1, tmp+1, tmp*2]:
        if value < 0 or value > max_value:
            continue
        if graph[value] != 0:
            continue
        graph[value] = graph[tmp] + 1
        queue.append(value)

if N == K:
    print(0)
else:
    print(graph[K])
