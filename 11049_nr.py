# 동적 계획법 문제
# Matrix chain multiplication
# mij = dp[i][k] + dp[k][j] + matrix[i][0] + matrix[j][0] + matrix[j][1]
MAX = 2147483647
N = int(input())
matrix = [None] + [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for length in range(2, N+1):
    for i in range(1, N-length+2):
        j = i + length - 1 
        dp[i][j] = MAX
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[j][1] * matrix[k][1])
print(dp[1][N])

