import heapq
import sys
heap = []

for _ in range(int(sys.stdin.readline().rstrip()):
    command = int(sys.stdin.readline().rstrip())
    if command == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1]) # (우선순위, 값)[1] = 값
    else:
        heapq.heappush(heap, (-command, command))  # (우선순위, 값)
    