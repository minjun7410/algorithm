N = int(input())
wine = []
dp = [0 for _ in range(N)]
for _ in range(N):
    wine.append(int(input()))
for index in range(N):
    if index == 0:
        dp[index] = wine[index]
    elif index == 1:
        dp[index] = wine[index] + dp[index-1]
    elif index == 2:
        zero = dp[index-1]
        one = wine[index] + wine[index-1]
        two = wine[index] + wine[index-2]
        dp[index] = max(zero, one, two)
    else:
        zero = dp[index-1]  # 현재 인덱스를 선택하지 않고 전 인덱스의 값과 전전 인덱스의 최대값을 구함
        one = wine[index] + wine[index-1] + dp[index-3]  # 피벗의 인덱스 - 1의 값과 - 3의 최대값을 더하는 것은 3번 연속 마실 수 없는 조건을 통과하기 위함
        two = wine[index] + dp[index-2]  # 피벗의 인덱스 - 2 의 최대값을 더한다는 것은 3번 연속으로 마실 수 없는 조건을 통과한다.
        dp[index] = max(zero, one, two)
if N == 1:
    print(dp[0])
elif dp[N-1] > dp[N-2]:  # 이 문제는 계단 오르기 문제와 다르게 마지막이 N으로 정해진 것이 아니므로 N과 N-1의 최대값을 비교해야한다.
    print(dp[N-1])
else:
    print(dp[N-2])