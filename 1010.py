def pascal(N, M):
    dp[0][0] = 1
    dp[1][0] = 1
    dp[1][1] = 1
    for i in range(2, N+1):
        dp[i][0] = 1
        for j in range(1, i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        dp[i][i] = 1
        
        
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    dp = [[0 for _ in range(M+1)] for _ in range(M+1)]
    pascal(M, N)
    print(dp[M][N])