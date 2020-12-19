N, M = map(int, input().split())
visit = []
def backtracking():
    if len(visit) == M:
        print(' '.join(map(str, visit)))
        return
    for i in range(1, N+1):
        if not(visit):
            visit.append(i)
            backtracking()
            visit.pop()
        elif visit[-1] < i:
            visit.append(i)
            backtracking()
            visit.pop()
backtracking()