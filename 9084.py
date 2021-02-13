# 동적계획법, 냅색 문제
# 금액에 따른 동전의 조합을 구하는 문제 -> 냅색
# dp[i][j] = dp[i][j-temp_coin](coin[i]를 마지막에 사용하여 j에 도달하는 경우의 수) + dp[i-1][j](coin[i]를 사용하지 않고 j에 도달한 경우의 수)
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    # input
    N = int(input())
    coin = [0] + list(map(int, input().split()))
    price = int(input())
    # answer
    dp = [[0] + [0 for _ in range(price)] for _ in range(N+1)]
    result = 0
    dp[0][0] = 1
    for i in range(1, N+1):
        temp_coin = coin[i]
        for j in range(1, price+1):
            if j - temp_coin < 0:
                continue
            dp[i][j] = dp[i][j-temp_coin] + dp[i-1][j-temp_coin]
        dp[]
    print(dp)