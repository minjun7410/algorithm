# 동적계획법을 이용하는 문제

# 나의 풀이
# N = 4 라면
# card = [입력받은 값 리스트]
# dp = [카드 1장만을 살 떄 최대값, 카드 2장만을 살 떄 최대값(1장 2개 가능), ''']
# dp[x] = max(card[x], dp[x-y] + card[y])
# O(n^2)
N = int(input())
card = list(map(int, input().split()))
dp = [0 for _ in range(N)]
for i in range(N):
    max_value = 0
    for j in range(i):
        max_value = max(max_value, dp[i-j-1] + card[j])
    dp[i] = max(card[i], max_value)
print(dp[-1])