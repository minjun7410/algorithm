N, M = map(int, input().split())
visit = []
visit_lst = []
def backtracking():
    if len(visit) == M and (not(visit_lst) or visit > visit_lst[-1]):
        print(' '.join(map(str, visit)))
        visit_lst.append(visit[:])
        return
    for i in range(1, N + 1):
        if not(visit) or visit[-1] <= i:
            visit.append(i)
            backtracking()
            visit.pop()
    return
backtracking()