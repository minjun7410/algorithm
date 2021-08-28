# 구현? dfs
# 조합이 되는 집합만 visited에 True로 기록해야하는 점에서
# 재귀로 dfs 사용했다.
# 가능한 집합을 발견하면 flag를 통해 visited를 False로 기록되지 않게 만들었다.

import sys
from collections import deque
input = sys.stdin.readline
INF = 987654321

# input
N = int(input())
arr = [0] + [int(input()) for _ in range(N)]

# solution
visited = [False for _ in range(N+1)]

def dfs(target, present):
    global flag
    if visited[present]: return
    visited[present] = True
    if target == present:
        flag = True
        return
    next = arr[present]
    dfs(target, next)
    if flag: return
    visited[present] = False
    return

for i in range(1, N+1):
    flag = False
    target = i
    dfs(target, arr[i])
# print
printer = []
sums = 0
for i in range(1, N+1):
    if visited[i] == True:
        sums += 1
        printer.append(i)
print(sums)
for value in printer:
    print(value)

