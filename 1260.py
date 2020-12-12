from collections import deque

def dfs(nodes, V):
    visited = []
    visit_need = deque([V])
    
    while visit_need:
        present = visit_need.popleft()
        if present not in visited:
            visited.append(present)
            visit_need = deque(nodes[present]) + visit_need
    return visited
def bfs(nodes, V):
    visited = []
    visit_need = deque([V])
    
    while visit_need:
        present = visit_need.popleft()
        if present not in visited:
            visited.append(present)
            visit_need.extend(nodes[present])
    return visited
N, M, V = map(int, input().split())  # N: 정점의 수 M: 간선의 수 V: 시작할 정점

nodes = {i: [] for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[a].sort()

    nodes[b].append(a)
    nodes[b].sort()

dfs_result = ' '.join(map(str, dfs(nodes, V)))
bfs_result = ' '.join(map(str, bfs(nodes, V)))
print(dfs_result)
print(bfs_result)