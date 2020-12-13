from collections import deque


result = -1

def dfs(nodes, V):
    global result
    visited = []
    visit_need = deque([V])
    while visit_need:
        node = visit_need.popleft()
        if node not in visited:
            result += 1
            visited.append(node)
            visit_need = deque(nodes[node]) + visit_need
    return visited

M = int(input())
N = int(input())
nodes = {i: [] for i in range(1, M+1)}

for _ in range(N):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
for n in range(1, M+1):
    nodes[n].sort()
visit = dfs(nodes, 1)
print(result)