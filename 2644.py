from collections import deque

def bfs(nodes, V, point):
    visited = []
    visit_need = deque([V])
    visit_distance = [0 for _ in range(len(nodes.keys()) + 1)]
    
    while visit_need:
        tmp = visit_need.popleft()
        if tmp not in visited:
            visited.append(tmp)
            visit_need = visit_need + deque(nodes[tmp])
            for i in nodes[tmp]:
                if visit_distance[i] != 0: continue
                visit_distance[i] = visit_distance[tmp] + 1
    return visit_distance[point]
M = int(input())

start, point = map(int, input().split())

N = int(input())
nodes = {i: [] for i in range(1, M+1)}
for _ in range(N):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
for i in range(1, M+1):
    nodes[i].sort()
result = bfs(nodes, start, point)
result = -1 if result == 0 else result
print(result)