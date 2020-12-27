N = int(input())
dp = [[100000000] * 3 for _ in range(N+1)]
dp[1][0] = dp[1][1] = dp[1][2] = 0

for i in range(2, N+1):
    if i % 3 == 0:
        dp[i][0] = min(dp[i // 3][0], dp[i // 3][1], dp[i // 3][2]) + 1
    if i % 2 == 0:
        tmp = i // 2
        dp[i][1] = min(dp[tmp][0], dp[tmp][1], dp[tmp][2]) + 1
    
    tmp = i - 1
    dp[i][2] = min(dp[tmp][0], dp[tmp][1], dp[tmp][2]) + 1
if N == 1:
    print("1")
else:
    print(min(dp[N]))