N = int(input())
sequence = list(map(int, input().split()))
dp = [0 for _ in range(N)]

for index in range(N):
    max_value = 0
    for miners in range(1, index + 1):
        target_index = index - miners
        if sequence[target_index] < sequence[index] and max_value < dp[target_index]:
            max_value = dp[target_index]
    dp[index] = max_value + 1

print(max(dp))