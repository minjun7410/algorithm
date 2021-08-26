# 구현? dfs

import sys
from collections import deque
input = sys.stdin.readline
INF = 987654321

# input
N = int(input())
arr = [0] + [int(input()) for _ in range(N)]

# solution
result = []
visited =[False for _ in range(N+1)]
def dfs(i):
    queue = deque([(i,)])
    target = i
    while queue:
        tmp = queue.popleft()
        now = tmp[-1]
        if visited[now]: continue
        else:
            visited[now] = True
            if arr[now] == target:
                result.extend(tmp)
                continue
            queue.appendleft(tmp+(arr[now],))
for i in range(1, N+1):
    dfs(i)
# print
print(result)
for tmp in result:
    print(tmp)


