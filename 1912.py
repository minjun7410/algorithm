N = int(input())
dp = list(map(int, input().split()))  # dp에 현 상황에서 가장 큰 수를 넣는다.
max_value = dp[0]
for index in range(1, len(dp)):
    if dp[index-1] + dp[index] < dp[index]:  # 이전 요소를 현재 요소와 더한것이 현재 요소보다 못한 값이면 현 상황에서 가질 수 있는 가장 큰 수는 현재 요소다
        max_value = dp[index] if dp[index] > max_value else max_value
        continue
    else:  # 만일 더한 것이 현재 요소보다 크면 가질 수 있는 가장 큰 수는 더한 값이다.
        dp[index] += dp[index-1]
        max_value = dp[index] if dp[index] > max_value else max_value

print(max_value)