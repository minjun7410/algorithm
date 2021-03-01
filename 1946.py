# 그리디 알고리즘
# 일단 모든 사원을 조사한다. (O(N))
# 단 각 사원의 합격 가능여부를 정할 때 모든 사원을 조사할 필요는 없고
# 두개의 최저 순위를 구해서 두개가 이를 넘는지, 넘으면 카운트하는 식으로 (이건 안됨, 이렇게 되면 답은 항상 N-1이 나온다.)
# 서류, 면접 1등을 각각 구한다.
# 서류의 경우 면접 순위를 면접의 경우 서류 순위를 구하고 이를 마지노선으로 한다.
# 각 지원자의 성적 중 하나라도 마지노선을 넘으면 카운트한다.
# 이것도 안됨
# 정렬 후 1에서 N까지 반복문을 돌림
# 1이 4라면 temp는 4
# 2가 3이면 temp > 3 그러므로 temp = 3 count += 1

import sys
input = sys.stdin.readline

# input

T = int(input())
for _ in range(T):
    N = int(input())
    count = 0
    
    # solution
    
    lst = [tuple(map(int, input().split())) for _ in range(N)]
    lst.sort(key = lambda x: x[0])
    marginot = N+1
    for value in lst:
        if value[1] < marginot:
            marginot = value[1]
            count += 1
    print(count)        