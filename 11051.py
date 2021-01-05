def binomial(n, k):  # 이항계수 파스칼의 정리 (파스칼의 삼각형)
    dp[0][0] = 1
    dp[1][0] = 1
    dp[1][1] = 1
    for i in range(2, n+1):
        dp[i][0] = 1
        for j in range(1, i):
            dp[i][j] = (dp[i-1][j-1]%10007 + dp[i-1][j]%10007)%10007
        dp[i][i] = 1


N, K = map(int, input().split())
dp = [[-1 for _ in range(N+1)] for _ in range(N+1)]
binomial(N, K)
print(dp[N][K])