from collections import deque
N, M = map(int, input().split())
def backtracking():
    visit = []
    visit_need = deque([[i] for i in range(1, N+1)])
    while visit_need:
        tmp = visit_need.popleft()
        if len(tmp) == M:
            print(' '.join(map(str, tmp)))
            continue
        visit_need.extendleft([tmp + [i] for i in reversed(range(1, N+1))])
backtracking()