# 브루트 포스
# 아무리 생각해도 맞는 알고리즘이 생각이 안나서 며칠 딜레이 되었다.
# 결국 문제 유형을 보았는데 브루트 포스.

# combinations라는 유용한 라이브러리 함수를 알아냈다.
# 번거로운 조합 리스트 생성을 도와준다.
# combinations("list", N)
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
chicken = []
homes = []
for i in range(N):
    for j, value in enumerate(map(int, input().split())):
        if value == 1:
            homes.append((i, j))
        elif value == 2:
            chicken.append((i, j))
chicken_com = list(combinations(chicken, M))
result = 987654321
for combi in chicken_com:
    sums = 0
    for home in homes:
        tmp = 987654321
        for c in combi:
            tmp = min(tmp, abs(home[0] - c[0])+abs(home[1] - c[1]))
        sums += tmp
    result = min(result, sums)
print(result)
