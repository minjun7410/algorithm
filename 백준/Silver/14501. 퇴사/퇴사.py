import sys
input = sys.stdin.readline
N = int(input())
dp = [0 for i in range(N+2)]
for i in range(1, N+1):
    t, p = map(int, input().split())
    dp[i] = dp[i-1] if dp[i-1] > dp[i] else dp[i]
    if i + t > N+1: continue
    else:
        if dp[i+t] < dp[i] + p:
            dp[i+t] = dp[i] + p
print(dp[N] if dp[N] > dp[N+1] else dp[N+1])