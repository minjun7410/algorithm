# 우선순위 큐 문제
# 묶음 중 가장 적은 수를 가진 묶음 2개를 묶어야 최소값이 나온다.
# 따라서 입력을 받을 때 최소 힙으로 입력을 받고 
# 마지막에 묶음이 1개가 남을 때까지 
# 묶음 2개를 더한 값을 result에 더하고 힙에 저장한다.
# 마지막 묶음 1개가 남았을 땐 반복문 조건문이 False
import sys
import heapq

input = sys.stdin.readline

#  input 
N = int(input())

#  solution
result = 0
heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()))
if N == 1:
    print(0)
else:
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        tmp = first + second
        result += tmp
        heapq.heappush(heap, tmp)
    print(result)

# N == 1 일때 비교 횟수가 0인것을 간과했다.
# 파이썬에 내장된 heapq 패키지를 사용해서 쉽게 풀었다.
# 힙을 자세히 배워볼 필요가 있다.