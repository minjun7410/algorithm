import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
dequeue = deque([i for i in range(1, N+1)])
count = 0
for target in map(int, sys.stdin.readline().split()):
    length = len(dequeue)
    if dequeue[0] == target:
        dequeue.popleft()
        continue
    if dequeue.index(target) < length // 2 + 1:
        while dequeue[0] != target:
            count += 1
            dequeue.append(dequeue.popleft())
    else:
        while dequeue[0] != target:
            count += 1
            dequeue.appendleft(dequeue.pop())
    dequeue.popleft()
print(count)