import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

counts = [0 for _ in range(1000001)]
for a in A:
    counts[a] += 1
result = [0 for _ in range(n)]
stack = deque([])
for i in range(n-1, -1, -1):
    number = A[i]
    count = counts[number]
    while stack:
        maxNum = A[stack[-1]]
        maxCount = counts[maxNum]
        if count >= maxCount: stack.pop()
        else: break
    if not(stack):
        result[i] = -1
    else:
        result[i] = A[stack[-1]]
    stack.append(i)
print(' '.join(map(str, result)))