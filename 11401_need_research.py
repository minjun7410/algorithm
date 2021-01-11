N, K = map(int, input().split())

MOD = 1000000007

dp = [1]


for i in range(1, N+1):
    tmp = dp[i-1] * i
    tmp %= MOD
    dp.append(tmp)

under = (dp[K] * dp[N-K]) % MOD  # n^p-1 = 1 (MOD p), n^p-2 = n^-1 (MOD p)
index = MOD - 2
tmp = 1
while index != 0:  # K!(N-K)! 의 MOD - 2 승을 구하는 과정 (페르마의 소정리)
    if index % 2 == 1:
        tmp *= under
        tmp %= MOD
    under = (under * under) % MOD
    index //= 2

result = (dp[N] * tmp) % MOD


print(result)