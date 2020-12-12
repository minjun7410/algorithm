


'''
T = int(input())
def isNear(array, m, n):
    if m+1 < M and array[m + 1][n] == 1:
        return False
    elif n+1 < N and array[m][n+1] == 1:
        return False
    else:
        return True

for t in range(T):
    M, N, K = map(int,input().split())
    count = 0
    array = [[0 for _ in range(N)] for _ in range(M)]
    #M은 가로 N은 세로
    for k in range(K):
        a, b = map(int, input().split())
        array[a][b] = 1
    for n in range(N):
        for m in range(M):
            if array[m][n] == 1:
                count += 1 if isNear(array, m, n) else 0
    print(count)
'''