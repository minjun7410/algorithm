# 그리디 알고리즘
# 일단 모든 사원을 조사한다. (O(N))
# 단 각 사원의 합격 가능여부를 정할 때 모든 사원을 조사할 필요는 없고
# 두개의 최저 순위를 구해서 두개가 이를 넘는지, 넘으면 카운트하는 식으로 (이건 안됨, 이렇게 되면 답은 항상 N-1이 나온다.)
# 서류, 면접 1등을 각각 구한다.
# 서류의 경우 면접 순위를 면접의 경우 서류 순위를 구하고 이를 마지노선으로 한다.
# 각 지원자의 성적 중 하나라도 마지노선을 넘으면 카운트한다.

import sys
input = sys.stdin.readline

# input

T = int(input())
for _ in range(T):
    N = int(input())
    count = 0
    # solution
    
    marginot_doc = None
    marginot_inter = None
    min_document = N+1
    min_interview = N+1
    applicants = []
    for index in range(N):
        doc, inter = map(int, input().split())
        if min_document > doc:
            min_document = doc
            marginot_inter = inter
        if min_interview > inter:
            min_interview = inter
            marginot_doc = doc
        applicants.append((doc, inter))
    for doc, inter in applicants:
        if doc < marginot_doc or inter < marginot_inter:
            count += 1
    print(count)        