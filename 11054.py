N = int(input())

sequence = list(map(int, input().split()))
sequence_reverse = list(reversed(sequence))

dp = [1 for _ in range(N)]
dp_reverse = [1 for _ in range(N)]

for index in range(N):
    for miners in range(1, index + 1):
        target_index = index - miners
        if sequence[target_index] < sequence[index]:
            dp[index] = max(dp[index], dp[target_index] + 1)
        if sequence_reverse[target_index] < sequence_reverse[index]:
            dp_reverse[index] = max(dp_reverse[index], dp_reverse[target_index] + 1)

max_value = 0

for i in range(N):
    if max_value < dp[i] + dp_reverse[N - i - 1]:
        max_value = dp[i] + dp_reverse[N - i - 1]
print(max_value - 1)