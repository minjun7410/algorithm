import sys
input = sys.stdin.readline

N = int(input())
constraint_list = list(map(int, input().split()))
result = constraint_list.pop()
dp = [0 for _ in range(21)]
dp[constraint_list[0]] = 1
number = 1
while number < N-1:
    present = [0 for _ in range(21)]
    for i, v in enumerate(dp):
        if v == 0: continue
        plus = i + constraint_list[number]
        minus = i - constraint_list[number]
        if plus < 21:
            present[plus] += dp[i]
        if minus >= 0:
            present[minus] += dp[i]

    number += 1
    dp = present[:]
print(dp[result])