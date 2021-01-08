import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
queue = deque([i for i in range(1, N+1)])
i = 0
while len(queue) != 1:
    if i % 2 == 0:
        queue.popleft()
    else:
        queue.append(queue.popleft())
    i += 1
print(queue[0])
