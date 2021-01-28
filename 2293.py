# 동적계획법 문제
# 0부터 k까지 반복한다.
# dp[i + coin[j]] += dp[i] (단 k >= i + coin[j])

import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
dp = [1] + [0 for _ in range(k)]
for coin in coins: # 두 반복문의 순서가 중요하다.
    for price_index in range(k): # 이런 순서를 가져야 중복된 동전의 구성을 피할 수 있다.
        if price_index + coin <= k:
            dp[price_index + coin] += dp[price_index]
print(dp[-1])