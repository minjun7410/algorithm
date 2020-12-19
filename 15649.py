N, M = map(int, input().split())
visit = []
def backtracking(N, M):
    if len(visit) == M:
        print(' '.join(map(str, visit)))
        return
    for i in range(1, N+1):
        if i not in visit:
            visit.append(i)
            backtracking(N, M)
            visit.pop()
backtracking(N, M)