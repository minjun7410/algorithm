N = int(input())
dp = [0 for _ in range(10)]  # 현재 계단의 마지막 위치 0 ~ 9 인 것들의 총 갯수
for i in range(1, 10):  # 0을 제외하고 처음 머무르는 위치 1씩 넣기
    dp[i] = 1

for _ in range(N - 1):
    new_dp = [0 for _ in range(10)]
    for index in range(10):
        if index == 0:  # index - 1가 0보다 작을 경우
            new_dp[index + 1] += dp[index]
        elif index == 9:  # index + 1가 9를 넘을 경우
            new_dp[index - 1] += dp[index]
        else:
            new_dp[index + 1] += dp[index]
            new_dp[index - 1] += dp[index]
    for i in range(10):
        dp[i] = new_dp[i] % 1000000000
print(sum(dp) % 1000000000)