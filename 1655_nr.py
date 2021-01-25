# 우선순위 큐, 힙은 최댓값, 최소값을 연속적으로 찾아내는데 특화된 자료구조이다.
# 1655 문제는 최대, 최소값이 아닌 중간값을 연속적으로 찾아내는 문제다.

# 문제 질문 : yukariko
# 중앙값을 기준으로 더 작은 값들을 모아둔것과, 더 큰값을 모아둔 집합을 나눠서 관리하고
#숫자가 추가될 때마다 중앙값과 집합을 갱신해주는 방법입니다.

import sys
import heapq

max_heap = []
min_heap = []
for _ in range(int(input())):
    num = int(sys.stdin.readline().rstrip())
    if len(max_heap) == len(min_heap):  # 참고할 때 가장 이해가 안됐었던 부분, 이렇게 되면 max_heap - min_heap 의 길이 차이가 1, 0, 1, 0 으로 고정이 된다
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, (num, num))
    
    if min_heap and max_heap[0][1] > min_heap[0][1]: # 이전에 max_heap 또는 min_heap에 한개의 요소를 push했으므로 max_heap의 루트와 min_heap의 루트를 비교해서 크면 교체한다. (단 min_heap에 요소가 존재할 시)
        tmp_max = heapq.heappop(max_heap)[1]
        tmp_min = heapq.heappop(min_heap)[1]
        heapq.heappush(min_heap, (tmp_max, tmp_max))
        heapq.heappush(max_heap, (-tmp_min, tmp_min))
    print(max_heap[0][1])
        