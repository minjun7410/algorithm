# 구현
# 3개 이상 교처를 허용하지 않으므로 타깃 연결선이 다른 모든 연결선에 얼마나 교차하는지만 검사하면 될것 같다.

# 조합 매서드를 불러서 사용
# 직사각형을 원으로 생각 (https://degurii.tistory.com/123)
# 이번 문제같이 표현이 어렵거나 설계하기 어려운 문제가 보이면
# 유연하게 대처해야 쉽게 풀 수 있다는 걸 암

import sys
from itertools import combinations
input = sys.stdin.readline

# input
N = int(input())
lines = []
for _ in range(N//2):
    x1, y1, x2, y2 = map(int, input().split())
    tmp = []
    for x, y in [(x1, y1), (x2, y2)]:
        if x == 1:
            tmp.append(y)
        elif x == 4:
            tmp.append(1000 + y)
        elif x == 2:
            tmp.append(2000 - y)
        else:
            tmp.append(3000 - y)
    if tmp[0] > tmp[1]:
        lines.append((tmp[1], tmp[0]))
    else:
        lines.append((tmp[0], tmp[1]))
counter = {i: 0 for i in lines}

# solution
lines_comb = combinations(lines, 2)
result = 0
def research(A, B):
    global result
    if A[0] <= B[0]:
        a = A[0]
        b = A[1]
        c = B[0]
        d = B[1]
    else:
        a = B[0]
        b = B[1]
        c = A[0]
        d = A[1]
    if a <= c and c <= b and b <= d:
        result += 1
        return True
    return False
for comb in lines_comb:
    boolean = research(comb[0], comb[1])
    if boolean:
        counter[comb[0]] += 1
        counter[comb[1]] += 1
print(result)
print(max(counter.values()))