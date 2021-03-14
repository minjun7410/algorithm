# BFS 문제
# 이분 그래프란 서로 다른 그룹의 정점이 간선으로 연결된 그래프라고 한다.(woovictory.github.io)
# 다시말해 어느 한 정점과 인접한 정점은 무조건 다른 그룹의 정점이어야 한다.
# BFS 또는 DFS로 풀 수 있을듯
# 하얀색, 검은색 구분지어서 인접한 정점은 무조건 다른 그룹의 정점이어야 하는 조건을 간단하게 만들어서 풀어봄
# 이전에 왔던 노드를 기억할 필요가 있어서 덱에 이전 노드의 위치를 넣었지만 visited가 0이 맞는지만 구분하면 되는 일이라 배제해도 될 뻔 했다.

# 첫번째 오답
# 모든 정점이 간선을 가지고 있지 않으며 정점의 모임?이 서로 독립되어 있는 경우를 생각하여 처음 BFS를 시작할 때 1만 조사하지 않고 모든 정점을 시작 정점으로 두고 조사하도록 for문을 추가하였다.

# 두번째 시간초과
# 모든 정점을 조사하는데 시간이 오래걸리고 이미 조사한 시작정점을 다시 BFS로 돌릴 필요가 없으므로(중복) visited 리스트를 for문 밖으로 내보내어서 중복을 없앴다.

# 세번째 AC

import sys
from collections import deque

input = sys.stdin.readline

# solution

def bfs():
    visited = [0 for _ in range(V+1)] # 0: 방문 X 1: 검은색 2: 하얀색
    for i in range(1, V+1): # i : 시작 정점
        if visited[i] != 0:
            continue
        queue = deque([(i, 0)]) # (현재 위치, 이전에 방문한 위치)
        visited[i] = 1
        while queue:
            present, before = queue.popleft()
            for future in nodes[present]:
                if visited[present] == visited[future]:  # 현재 색깔이 다음 노드 색깔과 같은 경우
                    return "NO"
                if visited[future] != 0: # 이미 방문했던 노드인 경우 ()
                    continue
                visited[future] = 1 if visited[present] == 2 else 2
                queue.append((future, before))
    return "YES"


# input

for _ in range(int(input())):
    V, E = map(int, input().split())
    nodes = {key:[] for key in range(1, V+1)}
    for _ in range(E):
        a, b = map(int, input().split())
        nodes[a].append(b)
        nodes[b].append(a)
    print(bfs())

# 정점의 간선과 이어진 정점들을 쌍방향으로 딕셔너리에 저장했다.
# visited 리스트는 다른 BFS문제와는 다르게 1차원 배열이다.
# 최소 이동거리를 구하는 것도 아니고 모든 노드를 조사한다는 점에서 DFS로도 풀 수 있을 것이다.