# 동적계획법
# i 가 조합의 수 k 가 더할 숫자 j가 현재 수 
# dp[i][j] += dp[i-1][j-k]

# input
N, K = map(int, input().split())
dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
dp[0][0] = 1
# answer
for i in range(K):
    for j in range(N+1):
        for k in range(N+1):
            if j + k > N:
                break
            dp[i+1][j+k] = (dp[i][j] + dp[i+1][j+k]) % 1000000000
print(dp[-1][-1])