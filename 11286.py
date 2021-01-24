# 절댓값이 작은 순으로 출력하는 힙 문제 (같을 경우 값이 작은 순)
# 절댓값이 같을 때 더 작은 수를 구분하는 것이 문제인데
# 나의 풀이는 양수일 때 +0.1으로 음수와 구별하면서 힙에 음수, 양수 순으로 입력되게 만듬
# pop을 할 떄는 1로 나누어지는 경우 음수이므로 -를 붙여서 프린트,
# 1로 나누어지지 않는 경우는 양수이므로 int()를 이용해서 정수로 표현.

import sys
import heapq
heap = []
for _ in range(int(sys.stdin.readline().rstrip())):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            y = heapq.heappop(heap)
            if y % 1 == 0:
                print(-(y))
            else:
                print(int(y))
        continue
    x = x + 0.1 if x > 0 else abs(x)
    heapq.heappush(heap, x)

    
#  다른 풀이
# 다른 사람의 풀이는 절대값이 같은 수일 때 \x\ = y (x < 0)
# 그리고 x^2 = y^2 임을 이용하여
# 힙에 push할 떄 (x^2, x)의 형식으로 저장한 후
# pop할 떄 튜플의 1번째 인자를 프린트한다.

#for i in range(int(sys.stdin.readline())):
#    num = int(sys.stdin.readline())
#    if num == 0:
#        if (len(heap) == 0):
#            print(0)
#        else:
#            res = heapq.heappop(heap)
#            print(res[1])
#    else:
#        heapq.heappush(heap, (num * num, num))