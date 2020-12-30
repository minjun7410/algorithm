first = input()
second = input()

dp = [[0 for _ in range(len(first)+1)] for _ in range(len(second)+1)]

for vertical in range(1, len(second)+1):
    for horizontal in range(1, len(first)+1):
        if second[vertical-1] == first[horizontal-1]:  # 문자가 같으면 dp 왼쪽, 위 값의 +1을 넣어준다. (단어의 중복을 의식)
            dp[vertical][horizontal] = dp[vertical-1][horizontal-1] + 1
        else:
            dp[vertical][horizontal] = max(dp[vertical-1][horizontal], dp[vertical][horizontal-1])

print(max(dp[-1]))