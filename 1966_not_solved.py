import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    documents = list(map(int, sys.stdin.readline().split()))
    queue = deque([i for i in range(N)])  # queue 인자의 중요도 = document[index]
    max_value = max(documents)
    result = 0
    while queue:
        result += 1
        if documents[queue[0]] == max_value:
            
            print(documents)
            print(queue)
            del documents[queue[0]]
            queue.popleft()
            if not(queue):
                break
            max_value = max(documents)
        else:
            queue.append(queue.popleft())
    print(result)
    