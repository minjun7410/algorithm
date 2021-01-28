# 동적계획법 문제
# dp 는 마지막 자리수에 해당하는(머무르는) 숫자를 인덱스로한다. 222 = dp[2]

N = int(input())
dp = [1 for _ in range(10)]
for index in range(1, N):
    new_dp = [0 for _ in range(10)]
    for digit in range(10):
        for i in range(digit, 10):
            new_dp[i] += dp[digit]
    for i in range(10):
        dp[i] = new_dp[i] % 10007
print(sum(dp) % 10007)