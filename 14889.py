from collections import deque
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

miner = 10000000
def dfs():
    global miner
    visit = []
    visit_need = deque([[i] for i in range(1, N+1)])
    while visit_need:
        tmp = visit_need.popleft()
        visit.append(tmp)
        if len(tmp) == N//2:
            a = calcul(tmp[:])
            other = [i for i in range(1, N+1) if i not in tmp]
            b = calcul(other[:])
            if miner > abs(a-b):
                miner = abs(a-b)
            continue
        for i in reversed([i for i in range(1, N+1) if i > tmp[-1]]):
                visit_need.appendleft(tmp + [i])
def calcul(tmp):
    sums = 0
    for i in tmp:
        for j in tmp:
            if j == i: continue
            sums += board[i-1][j-1]
    return sums
dfs()
print(miner)