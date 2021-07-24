# 우선 순위 큐 문제

# plan
# 1. 가방 최대 무게를 기준으로 오름차순으로 정렬한다.
# 2. 보석 무게를 기준으로 최대 힙을 만든다.
# 3. 가방 무게로 반복문을 돈다.
# 3-1. 우선 순위 큐를 도는데 if [가방 무게] < [보석 무게] continue
# 3-2. continue 하기 전에 다른 최소힙을 만들어서 저장한다.
# 3-3. 조건문을 통과하면 pop 하고 result += pop
# 3-4. 최소힙을 모두 pop해서 최대힙에 넣어줌 (가장 값이 큰 보석을 할당하고 힙에서 제외)
# 3-5. 힙을 모두 돌아도 조건문을 만족 못하면 break
# 4. return result

# 최대, 최소 힙 두개를 이용하는 풀이는 AC와 비슷했으나 보석의 기준으로한 최소힙,
# 가치를 기준으로한 최대힙을 사용한다는 점이 시간초과를 안할 수 있는 특징
# 즉, 가방 가용 무게보다 작은 보석의 무게를 가진 노드는 따로 POP해서 가치를 기준으로한 최대힙을 만들면
# 가방 무게보다 작은 보석의 최대 가치를 구할 수 있다는 것
# 이렇게 되면 다음 가방 무게를 조사할 때에도 힙을 따로 건들지 않아도 되니까 시간초과가 안남

# 계획했을 땐 (1)가방 무게에 (2)가장 큰 가치를 저장하고(3)나머지를 최대힙에 저장하는 식이었지만
# AC 풀이는  (1)가방 무게보다 (2)작은 보석을 꺼내서 (3)최대힙에 저장하는 식이다.

import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
heap_m = []
heap_v = []
for _ in range(N):
    M, V = map(int, input().split())
    heapq.heappush(heap_m, (M, V))
bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort()
result = 0

for bag in bags:
    while heap_m and heap_m[0][0] <= bag:
        M, V = heapq.heappop(heap_m)
        heapq.heappush(heap_v, (-V, M))
    if heap_v:
        result += heapq.heappop(heap_v)[0]
print(-result)
