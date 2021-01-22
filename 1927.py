import heapq
import sys
heap = []
for _ in range(int(sys.stdin.readline().rstrip())):
    command = int(sys.stdin.readline().rstrip())
    if command == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, command)